// var secondGranim = new Granim({
//   // element: "#second",
//   name: "second-gradient",
//   elToSetClassOn: "html",
//   direction: "top-bottom",
//   opacity: [1, 1],
//   image: {
//     source: "{%static 'images/course_back.jpg'%}",
//     stretchMode: ["stretch", "stretch"],
//     blendingMode: "overlay"
//   },
//   states: {
//     "default-state": {
//       gradients: [["#9C27B0", "#E91E63"], ["#009688", "#8BC34A"]],
//       transitionSpeed: 2000
//     }
//   }
// });

// function add_wish(user, course){
// function add_wish(){
//     alert("Добавлено");
//     // user.profile.add_to_wishes(course);
// }

// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
