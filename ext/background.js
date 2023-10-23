// background.js
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'send_data') {
      // Send data to your Django app
      fetch('http://localhost:8000/api/mydata/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify(request.data),
      })
      .then(response => response.json())
      .then(data => {
        console.log('Data sent successfully:', data);
        // Notify the extension popup (if needed)
        chrome.runtime.sendMessage({ action: 'receive_data', data });
      })
      .catch(error => console.error('Error sending data:', error));
    }
  });