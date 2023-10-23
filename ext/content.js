// content.js

function getCSRFToken() {
  const cookieName = 'csrftoken';
  const cookieValue = document.cookie.split(';')
      .map(cookie => cookie.trim())
      .find(cookie => cookie.startsWith(`${cookieName}=`));

  if (cookieValue) {
      return cookieValue.substring(cookieName.length + 1);
  }

  return null;
}

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === 'get_csrf_token') {
      const csrfToken = getCSRFToken();
      sendResponse({ csrfToken });
  }
});

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === "get_data") {
    // Collect data from the webpage
    const data = {
      
      imageUrl: document.querySelector("img").src,
      test: 'test'
    };

    // Send the data back to the extension
    chrome.runtime.sendMessage({ action: "send_data", data });
    console.log(data)
  }
});
