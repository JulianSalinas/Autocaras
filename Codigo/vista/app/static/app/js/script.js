 var loadFile = function (event) {
     var output = document.getElementById('output');
     output.src = URL.createObjectURL(event.target.files[0]);
 };

 $(document).ready(function () {
     $('input[type="checkbox"]').change(function () {
         if ($('input[type="url"]').attr('required')) {
             $('input[type="url"]').removeAttr('required');
         } else {
             $('input[type="url"]').attr('required', 'required');
         }
     });
 });
