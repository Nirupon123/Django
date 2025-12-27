const input = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const statusText = document.getElementById("status");
const uploadBtn = document.getElementById("uploadBtn");

let selectedFile = null;

input.addEventListener("change", () => {
  selectedFile = input.files[0];

  if (!selectedFile) return;

  preview.src = URL.createObjectURL(selectedFile);
  preview.style.display = "block";
  statusText.textContent = "";
});

uploadBtn.addEventListener("click", async () => {
  if (!selectedFile) {
    statusText.textContent = "Please select an image first";
    return;
  }

  uploadBtn.disabled = true;
  statusText.textContent = "Uploading...";

  const formData = new FormData();
  formData.append("image", selectedFile);

  try {
   const response = await fetch(
  "http://127.0.0.1:8000/store/Products/1/images/",
  {
    method: "POST",
    headers: {
      Authorization: "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY1ODk2Nzk1LCJpYXQiOjE3NjU4MTAzOTUsImp0aSI6ImFmMmZmZDVkNWI4NDQyNWI5ZDMyODEzOTAwMGM1ZGNhIiwidXNlcl9pZCI6IjEifQ.hYJh89aD9acIx-gKFEUI6AxKZfctzwgFT1SeYx3GvsM"
      // OR if you're using SimpleJWT:
      // Authorization: "Bearer YOUR_ACCESS_TOKEN"
    },
    body: formData
  }
);

   if (!response.ok) {
  const errorText = await response.text();
  throw new Error(errorText);
}


    statusText.textContent = "Upload successful ";
  } catch (error) {
  console.error(error.message);
  statusText.textContent = error.message;

  } finally {
    uploadBtn.disabled = false;
  }
});

