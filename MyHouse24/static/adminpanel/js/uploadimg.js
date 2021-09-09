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


function openContent(evt, TabInfo) {
    // Declare all variables
    var i, tab-panel, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tab-panel");
    for (i = 0; i < tab-panel.length; i++) {
        tab-panel[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}