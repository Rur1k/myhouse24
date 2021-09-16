function readURL(input, id) {
 if (input.files && input.files[0]) {
  var reader = new FileReader();

  reader.onload = function(e) {
   $(id).attr('src', e.target.result);
  }

  reader.readAsDataURL(input.files[0]);
 }
}

$("#image_1").change(function() {
 readURL(this, '#img1');
});
$("#image_2").change(function() {
 readURL(this, '#img2');
});
$("#image_3").change(function() {
 readURL(this, '#img3');
});
$("#image_4").change(function() {
 readURL(this, '#img4');
});
$("#image_5").change(function() {
 readURL(this, '#img5');
});
