$(document).ready(function() {
    var translateToAge; // Final target age for translation

    // Display the value which the range bar is hovering over on change
    $("#ageSlider").change(function() {
        $("#sliderValue").html(this.value);
        setAge(this.value)
    }).on("input", function() {
        $("#sliderValue").html(this.value);
        setAge(this.value)
    });


    // Grab target age for translation
    $('#translateButton').click(function (e) {
        translateTarget = getAge();
        console.log(translateTarget)
        // Todo: Send translateTarget age to backend function
    });


    // Function to set translateToAge to selected age
    function setAge(age) {
        translateToAge = age;
    }
    // Get translateToAge
    function getAge() {
        return translateToAge;
    }
});


  