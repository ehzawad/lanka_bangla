function addSuggestion(suggestions) {
    console.log("addSuggestion called with suggestions:", suggestions);
    const suggLength = suggestions.length;
    console.log("Number of suggestions:", suggLength);
    
    const suggestionsHTML = `
        <div class="singleCard">
            <div class="suggestions">
                <div class="menu"></div>
            </div>
        </div>
    `;
    console.log("Creating suggestions HTML:", suggestionsHTML);
    
    const $suggestions = $(suggestionsHTML)
        .appendTo(".chats")
        .hide()
        .fadeIn(1000);
    console.log("Suggestions appended to .chats");
    
    for (let i = 0; i < suggLength; i += 1) {
        console.log(`Adding suggestion ${i}:`, suggestions[i]);
        const { title, payload, type, url } = suggestions[i];
        
        if (type === 'urlLink' && url) {
            $(`<a href="${url}" target="_blank" rel="noopener noreferrer" class="menuChips" data-payload='${payload}'>${title}</a>`)
                .appendTo($suggestions.find(".menu"));
        } else {
            $(`<div class="menuChips" data-payload='${payload}'>${title}</div>`)
                .appendTo($suggestions.find(".menu"));
        }
    }

    console.log("All suggestions added, scrolling to bottom");
    scrollToBottomOfResults();
}

// Make sure to keep this part outside of any function
$(document).on("click", ".menu .menuChips", function (e) {
    console.log("Suggestion button clicked");
    const text = this.innerText;
    const payload = this.getAttribute("data-payload");
    console.log("Clicked button text:", text);
    console.log("Clicked button payload:", payload);
    
    if (this.tagName.toLowerCase() === 'a') {
        // If it's a link, let the default behavior happen (open in new tab)
        console.log("URL button clicked, opening link in new tab");
        // We don't prevent default here, allowing the link to open
    } else {
        e.preventDefault();
        setUserResponse(text);
        send(payload);
        console.log("Removing clicked suggestion's container");
        $(this).closest('.singleCard').remove();
    }
});