(function() {
    let paragraphs = documentElementsByTagName('p');
    for (let i = 0; i < paragraphs.length; i++) {
        paragraphs[i].innerHTML = 'cool';
    }
})();

