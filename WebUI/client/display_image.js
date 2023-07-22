const fileInput = document.getElementById('file');
const form = document.getElementById('order-form');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  alert('You have successfully submitted the image!');
  
  const formData = new FormData();
  formData.append('file', document.getElementById('file').files[0]);

  let response = await fetch("http://95.42.52.106:5677/submit", { method: "POST", body: formData });
  let data = await response.json();
  
  // Reset the form after submission
  form.reset();

});

// JavaScript
const fileInput1 = document.getElementById('file');
const form1 = document.getElementById('order-form');
const uploadedContainer = document.getElementById('uploaded-container');

fileInput1.addEventListener('change', () => {
  const file1 = fileInput1.files[0];

  if (file1) {
    // Remove any previously uploaded elements
    uploadedContainer.innerHTML = '';

    // Create a new division to display the uploaded photo
    const uploadedDiv = document.createElement('div');
    uploadedDiv.classList.add('uploaded-photo');

    // Create an image element and set its source to the uploaded photo
    const uploadedImage = document.createElement('img');
    uploadedImage.alt = 'Uploaded Photo';
    uploadedImage.style.padding = '10px'; // Add padding to the image
    uploadedImage.style.width = '50%'; 
    uploadedImage.style.height = '50%'; // Add padding to the image


    uploadedImage.src = URL.createObjectURL(file1); // Set the source to the uploaded file

    // Create a paragraph to display the image name
    const uploadedName = document.createElement('p');
    uploadedName.textContent = 'You have uploaded: ' + file1.name;

    // Append the image and paragraph to the div
    uploadedDiv.appendChild(uploadedImage);
    uploadedDiv.appendChild(uploadedName);

    // Append the div to the container
    uploadedContainer.appendChild(uploadedDiv);
  }
});

form1.addEventListener('reset', () => {
  // Remove any uploaded elements when the form is reset
  uploadedContainer.innerHTML = '';
});


let flag = true;

setInterval(async () => {
  let checkedText = await fetch("http://95.42.52.106:5677/check_text", { method: "GET" });
  let checkedTextData = await checkedText.json();
  if (checkedTextData.status !== "False") {
    if(flag === true){
      alert(checkedTextData.text);
      
      //set text to ''

      flag = false;
    } 
  }else{
    flag = true;
  }

}, 1000);

