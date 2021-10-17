var input = document.getElementById( 'browse-file' );
var graphTitle = document.getElementById( 'graph-title' );
var infoArea = document.getElementById( 'file-upload-filename' );
var uploadBtn = document.getElementById("upload");

input.addEventListener( 'change', showFileName );

function showFileName( event ) {
	// the change event gives us the input it occurred in 
  var input = event.srcElement;
  
  // the input has an array of files in the `files` property, each one has a name that you can use. We're just using the name here.
  var fileName = input.files[0].name;
  
  // use fileName however fits your app best, i.e. add it into a div
  infoArea.textContent = 'Selected File: ' + fileName;

}

function manageUploadBtn() {
    //checking if file and input field is not null
    if (infoArea.textContent != '' && graphTitle.value != '') {
            uploadBtn.style.background = '#07BF97';
            uploadBtn.disabled = false;
        }
    else {
        uploadBtn.style.background = '#a0beb881';
        uploadBtn.disabled = true;
        }
    }