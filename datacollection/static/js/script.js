const backgroundImages = [  
    '../images/bg_pothole1.jpg', 
    '../images/bg_pothole2.jpg', 
    '../images/bg_pothole3.jpg', 
    '../images/bg_pothole4.jpg', 
    '../images/bg_pothole5.jpg', 
    '../images/bg_pothole6.jpg',
    '../images/bg_pothole7.jpg'
];
const body = document.body;
const noOfImages = backgroundImages.length;
let imgIndex = Math.floor(Math.random() * noOfImages);  // gives a random first image
let cauroselDirection = 'forward';


function changeBackground() {
    body.style.background = `url(${backgroundImages[imgIndex]}) rgb(36, 36, 36) no-repeat center center/cover`;

    updateDirection();
    updateCurrentImageIndex();
}

function updateDirection(){
    if (imgIndex >= noOfImages-1){
        cauroselDirection = 'backward';
    } else if (imgIndex <= 0){
        cauroselDirection = 'forward';
    }
}

function updateCurrentImageIndex(){
    if (cauroselDirection === 'forward'){
        imgIndex++;
    } else {
        imgIndex--;
    }
}

changeBackground()
setInterval(changeBackground, 30000)  // change the background in every 30 second
