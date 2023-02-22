// Confirm Delete
function confirmDelete() {
  var name = getElementById("campaign-name")
  var result = confirm("Want to delete " + name + "?");
  if (result) {
      console.log("Deleted")
}
}

// Country Dropdown
function ausShow() {
    document.getElementById('austria').style.display = "block";
    document.getElementById('germany').style.display = "none";
    document.getElementById('france').style.display = "none";
    document.getElementById('italy').style.display = "none";
    document.getElementById('netherlands').style.display = "none";
    document.getElementById('uk').style.display = "none";
    document.getElementById('spain').style.display = "none";
    document.getElementById('ireland').style.display = "none";
 }
 function germShow() {
   document.getElementById('austria').style.display = "none";
   document.getElementById('germany').style.display = "block";
   document.getElementById('france').style.display = "none";
   document.getElementById('italy').style.display = "none";
   document.getElementById('netherlands').style.display = "none";
   document.getElementById('uk').style.display = "none";
   document.getElementById('spain').style.display = "none";
   document.getElementById('ireland').style.display = "none";
 }
 function franShow() {
   document.getElementById('austria').style.display = "none";
   document.getElementById('germany').style.display = "none";
   document.getElementById('france').style.display = "block";
   document.getElementById('italy').style.display = "none";
   document.getElementById('netherlands').style.display = "none";
   document.getElementById('uk').style.display = "none";
   document.getElementById('spain').style.display = "none";
   document.getElementById('ireland').style.display = "none";
 }
 function italyShow() {
   document.getElementById('austria').style.display = "none";
   document.getElementById('germany').style.display = "none";
   document.getElementById('france').style.display = "none";
   document.getElementById('italy').style.display = "block";
   document.getElementById('netherlands').style.display = "none";
   document.getElementById('uk').style.display = "none";
   document.getElementById('spain').style.display = "none";
   document.getElementById('ireland').style.display = "none";
 }
 function nethShow() {
   document.getElementById('austria').style.display = "none";
   document.getElementById('germany').style.display = "none";
   document.getElementById('france').style.display = "none";
   document.getElementById('italy').style.display = "none";
   document.getElementById('netherlands').style.display = "block";
   document.getElementById('uk').style.display = "none";
   document.getElementById('spain').style.display = "none";
   document.getElementById('ireland').style.display = "none";
 }
 function ukShow() {
   document.getElementById('austria').style.display = "none";
   document.getElementById('germany').style.display = "none";
   document.getElementById('france').style.display = "none";
   document.getElementById('italy').style.display = "none";
   document.getElementById('netherlands').style.display = "none";
   document.getElementById('uk').style.display = "block";
   document.getElementById('spain').style.display = "none";
   document.getElementById('ireland').style.display = "none";
 }
 function spainShow() {
   document.getElementById('austria').style.display = "none";
   document.getElementById('germany').style.display = "none";
   document.getElementById('france').style.display = "none";
   document.getElementById('italy').style.display = "none";
   document.getElementById('netherlands').style.display = "none";
   document.getElementById('uk').style.display = "none";
   document.getElementById('spain').style.display = "block";
   document.getElementById('ireland').style.display = "none";
 }
 function ireShow() {
   document.getElementById('austria').style.display = "none";
   document.getElementById('germany').style.display = "none";
   document.getElementById('france').style.display = "none";
   document.getElementById('italy').style.display = "none";
   document.getElementById('netherlands').style.display = "none";
   document.getElementById('uk').style.display = "none";
   document.getElementById('spain').style.display = "none";
   document.getElementById('ireland').style.display = "block";
 }
// function to show div when dropdown is selected
 var selectR = document.getElementById("selectR");
 selectR.addEventListener("change", function() {
   if (this.selectedIndex === 1) {
     document.getElementById('austria-d').style.display = 'block';
     document.getElementById('germany-d').style.display = 'none';
     document.getElementById('france-d').style.display = 'none';
     document.getElementById('italy-d').style.display = 'none';
     document.getElementById('uk-d').style.display = 'none';
     document.getElementById('spain-d').style.display = 'none';
     document.getElementById('netherlands-d').style.display = 'none';
     document.getElementById('ireland-d').style.display = 'none';
   } 
   else if (this.selectedIndex === 2) {
    document.getElementById('austria-d').style.display = 'none';
    document.getElementById('germany-d').style.display = 'block';
    document.getElementById('france-d').style.display = 'none';
    document.getElementById('italy-d').style.display = 'none';
    document.getElementById('uk-d').style.display = 'none';
    document.getElementById('spain-d').style.display = 'none';
    document.getElementById('netherlands-d').style.display = 'none';
    document.getElementById('ireland-d').style.display = 'none';
   }
   else if (this.selectedIndex === 3) {
    document.getElementById('austria-d').style.display = 'none';
    document.getElementById('germany-d').style.display = 'none';
    document.getElementById('france-d').style.display = 'block';
    document.getElementById('italy-d').style.display = 'none';
    document.getElementById('uk-d').style.display = 'none';
    document.getElementById('spain-d').style.display = 'none';
    document.getElementById('netherlands-d').style.display = 'none';
    document.getElementById('ireland-d').style.display = 'none';
   }
   else if (this.selectedIndex === 4) {
    document.getElementById('austria-d').style.display = 'none';
    document.getElementById('germany-d').style.display = 'none';
    document.getElementById('france-d').style.display = 'none';
    document.getElementById('italy-d').style.display = 'block';
    document.getElementById('uk-d').style.display = 'none';
    document.getElementById('spain-d').style.display = 'none';
    document.getElementById('netherlands-d').style.display = 'none';
    document.getElementById('ireland-d').style.display = 'none';
   }
   else if (this.selectedIndex === 5) {
    document.getElementById('austria-d').style.display = 'none';
    document.getElementById('germany-d').style.display = 'none';
    document.getElementById('france-d').style.display = 'none';
    document.getElementById('italy-d').style.display = 'none';
    document.getElementById('uk-d').style.display = 'block';
    document.getElementById('spain-d').style.display = 'none';
    document.getElementById('netherlands-d').style.display = 'none';
    document.getElementById('ireland-d').style.display = 'none';
   }
   else if (this.selectedIndex === 6) {
    document.getElementById('austria-d').style.display = 'none';
    document.getElementById('germany-d').style.display = 'none';
    document.getElementById('france-d').style.display = 'none';
    document.getElementById('italy-d').style.display = 'none';
    document.getElementById('uk-d').style.display = 'none';
    document.getElementById('spain-d').style.display = 'block';
    document.getElementById('netherlands-d').style.display = 'none';
    document.getElementById('ireland-d').style.display = 'none';
   }
   else if (this.selectedIndex === 7) {
    document.getElementById('austria-d').style.display = 'none';
    document.getElementById('germany-d').style.display = 'none';
    document.getElementById('france-d').style.display = 'none';
    document.getElementById('italy-d').style.display = 'none';
    document.getElementById('uk-d').style.display = 'none';
    document.getElementById('spain-d').style.display = 'none';
    document.getElementById('netherlands-d').style.display = 'block';
    document.getElementById('ireland-d').style.display = 'none';
   }
   else if (this.selectedIndex === 8) {
    document.getElementById('austria-d').style.display = 'none';
    document.getElementById('germany-d').style.display = 'none';
    document.getElementById('france-d').style.display = 'none';
    document.getElementById('italy-d').style.display = 'none';
    document.getElementById('uk-d').style.display = 'none';
    document.getElementById('spain-d').style.display = 'none';
    document.getElementById('netherlands-d').style.display = 'none';
    document.getElementById('ireland-d').style.display = 'block';
   }
 }, false);
