$(document).ready(function() {
    var translateToAge; // Final target age for translation
    var lastAge=-1; // Last requested aage

    // Grab target age and text for translation
    function update() {
        var translateData = {}
        translateData.age = getAge();
        translateData.text = $("#input").val();

        var thisAge=lastAge=translateData.age; // Age of this request (also setting lastAge)

        $.ajax({
            type: 'POST',
            url: '/translate',
            dataType: 'application/json',
            crossDomain: true,
            data: translateData,
            dataType: "json",
            success: function (translatedText) {
                if (thisAge==lastAge)
                    $("#output").val(translatedText.result);
            },
            error: function () {
              console.log("Translation failure.");
            }
          });
    }

    // Display the value which the range bar is hovering over on change
    $("#ageSlider").change(function() {
        $("#sliderValue").html(this.value);
        setAge(this.value)
        update()
    }).on("input", function() {
        $("#sliderValue").html(this.value);
        setAge(this.value)
        update()
    });

    // Initialize age
    $("#ageSlider").trigger("change");

    // Handle textarea changes
    var oldValue = ""
    $("#input").on("change keyup paste", function() {
        var curr=$(this).val();
        if (oldValue==curr) {
            return; // Don't process the same change twice
        }

        oldValue=curr;
        update();
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


