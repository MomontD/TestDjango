
// Отримуємо поточну дату
var currentDate = new Date();

// Отримуємо всі клітинки з класом "date-cell"
var dateCells = document.getElementsByClassName("government-date-cell");


// Перебираємо кожну клітинку і змінюємо її колір, якщо дата менша за поточну
for (var i = 0; i < dateCells.length; i++) {
    var cellDate = new Date(dateCells[i].textContent);

    if (cellDate < currentDate) {
      dateCells[i].style.background = "green";
    }
  }