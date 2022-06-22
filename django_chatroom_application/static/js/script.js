//Global variables:
let messagesContainer = document.getElementById('messagesContainer');
let messageInput = document.getElementById('messageInput');

async function sendMessage(token, user) {

    if (messageInput.value !== '') {

        let fd = new FormData();
        /* let token = document.querySelector('[name=csrfmiddlewaretoken]').value; */ //That's another way to get the value of the token.

        fd.append('textMessage', messageInput.value);
        fd.append('csrfmiddlewaretoken', token);

        try {

            messagesContainer.innerHTML += `

            <div class="message-container" id="beforeResponse">
                <span class="user-span"><b>${user}:</b></span>
                <span class="message-span"><i>${messageInput.value}</i></span>
                <span class="first-check">&#10004;</span>
                <span class="date-span">...<span>
            </div>

        `;

            let response = await fetch('/chatroom/', { //post call, but backend sends us a response with all the information of 
                //our new message just after the call
                method: 'POST',
                body: fd
            })

            let responseAsJson = await response.json();

            let parsedJson = JSON.parse(responseAsJson);

            let date = parsedJson.fields.created_at;

            let [year, month, day] = date.split('-');

            let result = [returnMonthInLetters(month), returnDayPlusComma(day), year].join(' ');

            let beforeResponse = document.getElementById('beforeResponse');

            beforeResponse.remove();

            messagesContainer.innerHTML += `
            
            <div class="message-container">
                <span class="user-span"><b>${user}:</b></span>
                <span class="message-span"><i>${messageInput.value}</i></span>
                <span class="first-check">&#10004;</span>
                <span class="second-check">&#10004;</span>
                <span class="date-span">${result}<span>
            </div>

        `;

            messageInput.value = '';

        } catch (e) {
            
            console.log(e);

        }

    } else {

        alert('It looks like you forgot to type your message...');

    }

}


function returnMonthInLetters(month) {
    
    let monthToNum = Number(month);
    
    let monthsArr = [['January', 1], ['February', 2], ['June', 6]];
    
    for (let i = 0; i < monthsArr.length; i++) {
        const monthInLetters = monthsArr[i][0];
        const monthValue = monthsArr[i][1];
        if (monthValue === monthToNum) {
            month = monthInLetters;
        }
    }

    return month;
}


function returnDayPlusComma(day) {

    return day + ',';

}


function searchForMessages() {
    // Declare variables
    var input, filter, container, span, i, txtValue;
    
    input = document.getElementById('searchBar');
    filter = input.value.toUpperCase();
    container = document.getElementById('messagesContainer');
    span = container.querySelectorAll('.message-span');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < span.length; i++) {
        //a = span[i].getElementsByTagName("a")[0];
        txtValue = span[i].textContent || span[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            let element = span[i];
            let parentDiv = element.parentNode;
            parentDiv.classList.remove('d-none');
        } else {
            let element = span[i];
            let parentDiv = element.parentNode;
            parentDiv.classList.add('d-none');
        }
    }

}