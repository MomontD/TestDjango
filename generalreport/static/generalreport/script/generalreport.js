
document.addEventListener('DOMContentLoaded', function() {

    let divDepositsSum = document.querySelector('.div_deposits_sum');
    let divDepositsTitle = document.querySelector(".div_deposits_title")
    let divDepositsProfit = document.querySelector(".div_deposits_profit")
    let depositsSum = parseInt(divDepositsSum.dataset.depositsSum);

    let divGovernmentsSum = document.querySelector('.div_governments_sum');
    let divGovernmentsTitle = document.querySelector(".div_governments_title")
    let divGovernmentsProfit = document.querySelector(".div_governments_profit")
    let governmentsSum = parseInt(divGovernmentsSum.dataset.governmentsSum);

    let divLoansSum = document.querySelector('.div_loans_sum');
    let divLoansTitle = document.querySelector(".div_loans_title")
    let divLoansProfit = document.querySelector(".div_loans_profit")
    let loansSum = parseInt(divLoansSum.dataset.loansSum);

    let capital = depositsSum + governmentsSum + loansSum
    let investmentRate = (investmentSum,capital) => {
        return Math.round((investmentSum / capital) * 100)
    }

    if (depositsSum !== 0) {
        let depositsRate = investmentRate(depositsSum,capital)
        divDepositsSum.style.width = depositsRate + '%';
        divDepositsTitle.style.width = depositsRate + '%';
        divDepositsProfit.style.width = depositsRate + '%';
        let existingDepositsTitle = divDepositsTitle.querySelector('h5').textContent.trim();
        divDepositsTitle.querySelector('h5').textContent = `${existingDepositsTitle} , ${depositsRate}%`;
    }

    if (governmentsSum !== 0) {
        let governmentsRate = investmentRate(governmentsSum, capital)
        divGovernmentsSum.style.width = governmentsRate + '%';
        divGovernmentsTitle.style.width = governmentsRate + '%';
        divGovernmentsProfit.style.width = governmentsRate + '%';
        let existingGovernmentsTitle = divGovernmentsTitle.querySelector('h5').textContent.trim();
        divGovernmentsTitle.querySelector('h5').textContent = `${existingGovernmentsTitle} , ${governmentsRate}%`;
    }

    if (loansSum !==0) {
        let loansRate = investmentRate(loansSum, capital)
        console.log(loansRate)
        divLoansSum.style.width = loansRate + '%';
        divLoansTitle.style.width = loansRate + '%';
        divLoansProfit.style.width = loansRate + '%';
        let existingLoansTitle = divLoansTitle.querySelector('h5').textContent.trim();
        divLoansTitle.querySelector('h5').textContent = `${existingLoansTitle} , ${loansRate}%`;
    }

})