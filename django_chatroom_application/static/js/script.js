let messagesContainer = document.getElementById('messagesContainer');
let messageInput = document.getElementById('messageInput');

async function sendMessage(token, user) {

    let fd = new FormData();
    //let token = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fd.append('textMessage', messageInput.value);
    fd.append('csrfmiddlewaretoken', token);

    try {

        messagesContainer.innerHTML += `
        <div id="beforeResponse">
            <b>${user}:</b> <span style="color: grey;">${messageInput.value}</span> <span class="message-date">(DATE)<span>
        </div>
    
        `;

        let response = await fetch('/chatroom/', { //post call, but backend sends us a response with all the information of 
                                                    //our new message just after the call
            method: 'POST',
            body: fd
        })

        //Now we take from the response what we need for our template view.

        let responseAsJson = await response.json();
        
        console.log(JSON.parse(responseAsJson))

        console.log('succes');

        let beforeResponse = document.getElementById('beforeResponse');

        beforeResponse.remove();

        messagesContainer.innerHTML += `
        <div>
            <b>${user}:</b> <span>${messageInput.value}</span> <span class="message-date">(DATE)<span>
        </div>
    
        `;

      
    } catch (e) {
        console.log(e);
    }

}