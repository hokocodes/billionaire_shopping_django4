// background.js

// Define the function to send data
function sendData(data) {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      chrome.tabs.sendMessage(tabs[0].id, { action: 'send_data', data });
  });
}

// Use chrome.runtime.sendMessage to communicate with content scripts
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === 'send_data') {
      // Get CSRF token from content script
      chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
          chrome.tabs.sendMessage(tabs[0].id, { action: 'get_csrf_token' }, function(response) {
              const csrfToken = response.csrfToken;

              if (csrfToken) {
                  // Send data to your Django app
                  fetch('http://localhost:8000/api/mydata/', {
                      method: 'POST',
                      headers: {
                          'Content-Type': 'application/json',
                          'X-CSRFToken': csrfToken,
                          'X-Referer': 'localhost:8000',
                      },
                      body: JSON.stringify(request.data),
                  })
                  .then(response => response.json())
                  .then(data => {
                      console.log('Data sent successfully:', data);
                      // Notify the extension popup (if needed)
                      chrome.runtime.sendMessage({ action: 'receive_data', data });
                      sendResponse({ farewell: 'Data sent successfully' });
                  })
                  .catch(error => {
                      console.error('Error sending data:', error);
                      sendResponse({ farewell: 'Error sending data' });
                  });
              } else {
                  console.error('CSRF token not found.');
                  sendResponse({ farewell: 'CSRF token not found' });
              }
          });
      });

      // Return true to indicate that you want to use sendResponse asynchronously
      return true;
  }
});
