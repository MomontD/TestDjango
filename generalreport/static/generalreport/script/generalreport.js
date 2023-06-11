
document.addEventListener('DOMContentLoaded', function() {

    let divDepositsSum = document.querySelector('.div_deposits_sum');
    let divDepositsTitle = document.querySelector(".div_deposits_title")
    let divDepositsRate = document.querySelector(".div_deposits_rate")
    let depositsSum = parseInt(divDepositsSum.dataset.depositsSum);

    let divGovernmentsSum = document.querySelector('.div_governments_sum');
    let divGovernmentsTitle = document.querySelector(".div_governments_title")
    let divGovernmentsRate = document.querySelector(".div_governments_rate")
    let governmentsSum = parseInt(divGovernmentsSum.dataset.governmentsSum);

    let divLoansSum = document.querySelector('.div_loans_sum');
    let divLoansTitle = document.querySelector(".div_loans_title")
    let divLoansRate = document.querySelector(".div_loans_rate")
    let loansSum = parseInt(divLoansSum.dataset.loansSum);

    let capital = depositsSum + governmentsSum + loansSum
    let investmentRate = (investmentSum,capital) => {
        return Math.round((investmentSum / capital) * 100)
    }

    if (depositsSum !== 0) {
        let depositsRate = investmentRate(depositsSum,capital)
        divDepositsSum.style.width = depositsRate + '%';
        divDepositsTitle.style.width = depositsRate + '%';
        divDepositsRate.style.width = depositsRate + '%';
        // let existingDepositsTitle = divDepositsTitle.querySelector('h5').textContent.trim();
        divDepositsRate.querySelector('h5').textContent = `${depositsRate}%`;
    }

    if (governmentsSum !== 0) {
        let governmentsRate = investmentRate(governmentsSum, capital)
        divGovernmentsSum.style.width = governmentsRate + '%';
        divGovernmentsTitle.style.width = governmentsRate + '%';
        divGovernmentsRate.style.width = governmentsRate + '%';
        // let existingGovernmentsTitle = divGovernmentsTitle.querySelector('h5').textContent.trim();
        divGovernmentsRate.querySelector('h5').textContent = `${governmentsRate}%`;
    }

    if (loansSum !==0) {
        let loansRate = investmentRate(loansSum, capital)
        divLoansSum.style.width = loansRate + '%';
        divLoansTitle.style.width = loansRate + '%';
        divLoansRate.style.width = loansRate + '%'
        // let existingLoansTitle = divLoansTitle.querySelector('h5').textContent.trim();
        divLoansRate.querySelector('h5').textContent = `${loansRate}%`;
    }

})