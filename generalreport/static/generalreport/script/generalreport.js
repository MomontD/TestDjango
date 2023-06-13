// Робочий варіант побудови динамічної таблиці по колонками відповідно до суми , %

// document.addEventListener('DOMContentLoaded', function() {
//
//     let investmentRate = (investmentSum,capital) => {
//         return Math.round((investmentSum / capital) * 100)
//     }
//
//     let investmentProfitRate = (investmentProfit,totalProfit) => {
//         return Math.round((investmentProfit/totalProfit) * 100)
//     }
//
//     let depositsSum = 0
//     let depositsProfit = 0
//     if (document.querySelector('.div_deposits_sum')) {
//         divDepositsSum = document.querySelector('.div_deposits_sum');
//         divDepositsProfit = document.querySelector(".div_deposits_profit")
//         depositsSum = parseInt(divDepositsSum.dataset.depositsSum);
//         depositsProfit = parseInt(divDepositsProfit.dataset.depositsProfit);
//     }
//
//     let governmentsSum = 0
//     let governmentsProfit = 0
//     if (document.querySelector('.div_governments_sum')) {
//         divGovernmentsSum = document.querySelector('.div_governments_sum');
//         divGovernmentsProfit = document.querySelector(".div_governments_profit")
//         governmentsSum = parseInt(divGovernmentsSum.dataset.governmentsSum);
//         governmentsProfit = parseInt(divGovernmentsProfit.dataset.governmentsProfit);
//     }
//
//     let loansSum = 0
//     let loansProfit = 0
//     if (document.querySelector('.div_loans_sum')) {
//         divLoansSum = document.querySelector('.div_loans_sum');
//         divLoansProfit = document.querySelector(".div_loans_profit")
//         loansSum = parseInt(divLoansSum.dataset.loansSum);
//         loansProfit = parseInt(divLoansProfit.dataset.loansProfit);
//     }
//
//     let capital = depositsSum + governmentsSum + loansSum
//
//     let totalProfit = depositsProfit + governmentsProfit + loansProfit
//
//     if (depositsSum) {
//         let depositsRate = investmentRate(depositsSum,capital)
//         let depositsProfitRate = investmentProfitRate(depositsProfit,totalProfit)
//         let divDepositsTitle = document.querySelector(".div_deposits_title")
//         divDepositsSum.style.width = depositsRate + '%';
//         divDepositsTitle.style.width = depositsRate + '%';
//         divDepositsProfit.style.width = depositsProfitRate + '%';
//         let existingDepositsTitle = divDepositsTitle.querySelector('h5').textContent.trim();
//         divDepositsTitle.querySelector('h5').textContent = `${existingDepositsTitle} , ${depositsRate}%`;
//         let existingDepositsProfit = divDepositsProfit.querySelector('h5').textContent.trim();
//         divDepositsProfit.querySelector('h5').textContent = `${existingDepositsProfit} (${depositsProfitRate}%)`;
//     }
//
//     if (governmentsSum) {
//         let governmentsRate = investmentRate(governmentsSum, capital)
//         let governmentsProfitRate = investmentProfitRate(governmentsProfit, totalProfit)
//         let divGovernmentsTitle = document.querySelector(".div_governments_title")
//         divGovernmentsSum.style.width = governmentsRate + '%';
//         divGovernmentsTitle.style.width = governmentsRate + '%';
//         divGovernmentsProfit.style.width = governmentsProfitRate + '%';
//         let existingGovernmentsTitle = divGovernmentsTitle.querySelector('h5').textContent.trim();
//         divGovernmentsTitle.querySelector('h5').textContent = `${existingGovernmentsTitle} , ${governmentsRate}%`;
//         let existingGovernmentsProfit = divGovernmentsProfit.querySelector('h5').textContent.trim();
//         divGovernmentsProfit.querySelector('h5').textContent = `${existingGovernmentsProfit} (${governmentsProfitRate}%)`;
//     }
//
//     if (loansSum) {
//         let loansRate = investmentRate(loansSum, capital)
//         let loansProfitRate = investmentProfitRate(loansProfit, totalProfit)
//         let divLoansTitle = document.querySelector(".div_loans_title")
//         divLoansSum.style.width = loansRate + '%';
//         divLoansTitle.style.width = loansRate + '%';
//         divLoansProfit.style.width = loansProfitRate + '%';
//         let existingLoansTitle = divLoansTitle.querySelector('h5').textContent.trim();
//         divLoansTitle.querySelector('h5').textContent = `${existingLoansTitle} , ${loansRate}%`;
//         let existingLoansProfit = divLoansProfit.querySelector('h5').textContent.trim();
//         divLoansProfit.querySelector('h5').textContent = `${existingLoansProfit} (${loansProfitRate}%)`;
//     }
//
// })