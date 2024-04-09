let uuid;
let lastImageDate;
const myPopup = document.getElementById('imagePopUp');

async function load() {
  //get the uuid
  uuid = localStorage.getItem('uuid');
  if (!uuid) {
    const response = await fetch('/api/getId');
    const data = await response.json();
    uuid = data.id;
    localStorage.setItem('uuid', uuid);
  }

  const response = await fetch('/api/getLastDate?id=' + uuid);
  const data = await response.json();
  lastImageDate = new Date(data.date * 1000);
  if (lastImageDate)
    document.getElementById(
      'last-image-date'
    ).innerText = `Your last upload was on: ${lastImageDate.toLocaleString()}`;
  else
    document.getElementById(
      'last-image-date'
    ).innerText = `No images on server yet`;
}

load();
document.getElementById('uuid-desc').innerText = `Your UUID is: ${uuid}`;

async function uploadFiles(form, e) {
  e.preventDefault();
  const formData = new FormData(form);
  formData.append('id', uuid);

  myPopup.innerHTML = '';
  myPopup.style.display = 'block';
  const progressBar = document.createElement('div');
  progressBar.style.setProperty('--width', '0%');
  progressBar.style.display = 'block';
  progressBar.classList.add('progressBar');
  myPopup.appendChild(progressBar);

  const response = await fetch('/api/upload', {
    method: 'POST',
    body: formData,
    onUploadProgress: function (progressEvent) {
      const progress = Math.round(
        (progressEvent.loaded / progressEvent.total) * 100
      );
      progressBar.style.setProperty('--width', progress + '%');
    },
  });

  progressBar.style.display = 'none';
  myPopup.style.display = 'none';

  const data = await response.json();
  if (data.success) {
    lastImageDate = new Date(data.date * 1000);
    document.getElementById(
      'last-image-date'
    ).innerText = `Your last upload was on: ${lastImageDate.toLocaleString()}`;

    alertUser('Image uploaded successfully', 'green');

    const chosenImages = document.querySelector(
      '.chosenImages:not(.currentImages)'
    );
    chosenImages.innerHTML = '';
    loadImages();
  } else {
    alertUser(data.error, 'red');
  }
}

document.getElementById('imageInput').addEventListener('change', (e) => {
  const files = e.target.files;
  const chosenImages = document.querySelector(
    '.chosenImages:not(.currentImages)'
  );
  chosenImages.innerHTML = '';
  for (let i = 0; i < files.length; i++) {
    const img = document.createElement('img');
    img.classList.add('chosenImage');
    img.src = URL.createObjectURL(files[i]);
    chosenImages.appendChild(img);

    img.addEventListener('click', () => {
      showImage(files[i]);
    });
  }
});

myPopup.addEventListener('click', (e) => {
  if (!e.target.classList.contains('targetImage'))
    myPopup.style.display = 'none';
});

function showImage(file) {
  const reader = new FileReader();
  reader.onload = function (e) {
    showImageLink(e.target.result);
  };
  reader.readAsDataURL(file);
}

function showImageLink(image) {
  const popup = myPopup;
  popup.innerHTML = '';

  const img = document.createElement('img');
  img.classList.add('targetImage');
  img.src = image;
  popup.appendChild(img);

  popup.style.display = 'flex';
}

function loadImages() {
  fetch('/api/getImages?id=' + uuid)
    .then((response) => response.json())
    .then((data) => {
      const currentImages = document.querySelector('.currentImages');
      currentImages.innerHTML = '';
      data.images.forEach((image) => {
        const img = document.createElement('img');
        img.classList.add('chosenImage');
        img.src = '/api/getImage/' + image + '?id=' + uuid;
        currentImages.appendChild(img);

        img.addEventListener('click', () => {
          showImageLink('/api/getImage/' + image + '?id=' + uuid);
        });
      });
    });
}

loadImages();

function alertUser(message, color) {
  const alert = document.createElement('p');
  alert.classList.add('alert');
  alert.style.backgroundColor = color;
  alert.innerText = message;
  document.body.appendChild(alert);
  setTimeout(() => {
    alert.remove();
  }, 5000);
}
