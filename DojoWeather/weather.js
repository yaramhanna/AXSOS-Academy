
const cookieAlert = document.querySelector(".cookieAlert");
const button = document.querySelector(".btn");

button.addEventListener ("click" , function(){
    cookieAlert.remove()
})

const tempSelect = document.querySelector("select");
const temperatures = document.querySelectorAll(".R, .L");

tempSelect.addEventListener("change", function() {

    for (let i = 0; i < temperatures.length; i++) {

        let temp = parseInt(temperatures[i].textContent);

        if (tempSelect.value === "C") {
            temp = (temp - 32) * 5 / 9;
        } else {
            temp = (temp * 9 / 5) + 32;
        }

        temperatures[i].textContent = Math.round(temp) + "°";
    }

});