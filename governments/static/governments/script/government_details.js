
// Отримуємо поточну дату
let currentDate = new Date();

// Отримуємо всі клітинки з класом "date-cell"
let dateCells = document.getElementsByClassName("government-date-cell");
let typeCells = document.getElementsByClassName("government-type-cell");
let paymentCells = document.getElementsByClassName("government-payment-cell")


// Перебираємо кожну клітинку і змінюємо її колір, якщо дата менша за поточну
for (var i = 0; i < dateCells.length; i++) {
    var cellDate = new Date(dateCells[i].textContent);

    if (cellDate < currentDate) {
      dateCells[i].style.background = "green";
      typeCells[i].style.background = "green";
      paymentCells[i].style.background = "green";

    }
  }