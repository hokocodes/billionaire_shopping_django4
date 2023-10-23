// content.js

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
