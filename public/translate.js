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

    $("#ageSlider").trigger("change");

    // Grab target age and text for translation
    $('#translateButton').click(function (e) {
        var translateData = {}
        translateData.age = getAge();
        translateData.text = $("#input").val(); 

        $.ajax({
            type: 'POST',
            url: '/translate',
            dataType: 'application/json',
            crossDomain: true,
            data: translateData,
            dataType: "json",
            success: function (translatedText) {
                $("#output").val(translatedText.result);
            },
            error: function () {
              console.log("Translation failure.");
            }
          });
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


  