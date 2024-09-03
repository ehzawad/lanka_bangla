// Add this at the beginning of your chat.js file
(function() {
    // Create a style element
    var style = document.createElement('style');
    // Remove the type attribute
    style.innerHTML = `
        #chats {
            overflow-y: scroll;
            scrollbar-width: thin;
            scrollbar-color: rgba(0, 0, 0, 0.2) transparent;
        }
        #chats::-webkit-scrollbar {
            width: 6px;
        }
        #chats::-webkit-scrollbar-track {
            background: transparent;
        }
        #chats::-webkit-scrollbar-thumb {
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 3px;
        }
        #chats::-webkit-scrollbar-thumb:hover {
            background-color: rgba(0, 0, 0, 0.3);
        }
    `;
    // Append the style element to the head
    document.head.appendChild(style);
})();



// Global variables
const converter = new showdown.Converter();
const fadeTimeout = 500;
let isNearBottom = true;

// Scrolling functions
function isUserNearBottom() {
    const chatContainer = document.getElementById("chats");
    const threshold = 100; // pixels from bottom
    return chatContainer.scrollHeight - chatContainer.scrollTop - chatContainer.clientHeight < threshold;
}

function scrollToBottomOfResults() {
    const chatContainer = document.getElementById("chats");
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function updateChatScroll() {
    if (isNearBottom) {
        scrollToBottomOfResults();
    }
}

// Call this function whenever new content is added
function handleNewContent() {
    isNearBottom = isUserNearBottom();
    updateChatScroll();
}

// User response function
function setUserResponse(message) {
    const user_response = `
        <div class="userAvatar">
            <div class="userAvatar-image">
                <img src='./static/img/userAvatar.png'>
            </div>
            <p class="userMsg">${message}</p>
        </div>
        <div class="clearfix"></div>
    `;
    $(user_response).appendTo(".chats").show("slow");

    $(".usrInput").val("");
    handleNewContent();
    showBotTyping();
}

// Bot response functions
function getBotResponse(text) {
    return `<img class="botAvatar" src="./static/img/bot-ai-logo.png"/><span class="botMsg">${text}</span><div class="clearfix"></div>`;
}

function displayChatbotMessage(buttonsData) {
    const { text, type } = buttonsData[0] || buttonsData;
    
    if (type && text) {
        let html = converter.makeHtml(text);
        html = html
            .replaceAll("<p>", "")
            .replaceAll("</p>", "")
            .replaceAll("<strong>", "<b>")
            .replaceAll("</strong>", "</b>");
        html = html.replace(/(?:\r\n|\r|\n)/g, "<br>");
        
        let botResponse = '';
        
        if (html.includes("<blockquote>") || 
            html.includes("<img") || 
            html.includes("<pre") || 
            html.includes("<code>") ||
            html.includes("<ul") ||
            html.includes("<ol") ||
            html.includes("<li") ||
            html.includes("<h3")) {
            
            if (html.includes("<blockquote>") || 
                html.includes("<ul") ||
                html.includes("<ol") ||
                html.includes("<li") ||
                html.includes("<h3")) {
                html = html.replaceAll("<br>", "");
            }
            
            if (html.includes("<img")) {
                html = html.replaceAll("<img", '<img class="imgcard_mrkdwn" ');
            }
            
            botResponse = getBotResponse(html);
        } else {
            botResponse = `
                <div class="botAvatar">
                    <div class="botAvatar-image">
                        <img src="./static/img/disha.svg"/>
                    </div>
                    <p class="botMsg">${html}</p>
                </div>
                <div class="clearfix"></div>
            `;
        }
        
        $(botResponse).appendTo(".chats").hide().fadeIn(fadeTimeout);
        handleNewContent();
    }
}

function setBotResponse(response) {
    setTimeout(() => {
        hideBotTyping();
        if (response.length < 1) {
            const fallbackMsg = "I am facing some issues, please try again later!!!";
            const BotResponse = `
                <div class="botAvatar">
                    <div class="botAvatar-image">
                        <img src="./static/img/disha.svg"/>
                    </div>
                    <p class="botMsg">${fallbackMsg}</p>
                </div>
                <div class="clearfix"></div>`;
            $(BotResponse).appendTo(".chats").hide().fadeIn(fadeTimeout);
        } else {
            response.forEach((res) => {
                if (res.text) {
                    let html = converter.makeHtml(res.text);
                    html = html
                        .replaceAll("<p>", "")
                        .replaceAll("</p>", "")
                        .replaceAll("<strong>", "<b>")
                        .replaceAll("</strong>", "</b>");
                    html = html.replace(/(?:\r\n|\r|\n)/g, "<br>");

                    const botResponse = `
                        <div class="botAvatar">
                            <div class="botAvatar-image">
                                <img src="./static/img/disha.svg"/>
                            </div>
                            <p class="botMsg">${html}</p>
                        </div>
                        <div class="clearfix"></div>
                    `;
                    $(botResponse).appendTo(".chats").hide().fadeIn(fadeTimeout);
                }

                if (res.buttons) {
                    addSuggestion(res.buttons);
                }

                if (res.image) {
                    const BotResponse = `<div class="singleCard"><img class="imgcard" src="${res.image}"></div><div class="clearfix">`;
                    $(BotResponse).appendTo(".chats").hide().fadeIn(fadeTimeout);
                }

                if (res.attachment && res.attachment.type === "video") {
                    const video_url = res.attachment.payload.src;
                    const BotResponse = `<div class="video-container"><iframe src="${video_url}" frameborder="0" allowfullscreen></iframe></div>`;
                    $(BotResponse).appendTo(".chats").hide().fadeIn(fadeTimeout);
                }

                if (res.custom) {
                    const { payload } = res.custom;
                    
                    if (payload === "quickReplies") {
                        showQuickReplies(res.custom.data);
                    } else if (payload === "pdf_attachment") {
                        renderPdfAttachment(res);
                    } else if (payload === "dropDown") {
                        renderDropDwon(res.custom.data);
                    } else if (payload === "location") {
                        getLocation();
                    } else if (payload === "cardsCarousel") {
                        showCardsCarousel(res.custom.data);
                    } else if (payload === "chart") {
                        createChart(res.custom.data);
                    } else if (payload === "collapsible") {
                        createCollapsible(res.custom.data);
                    } else if (payload === "buttonsPayload") {
                        showButtons(res.custom.data);
                    } else if (payload === "urlLink") {
                        showUrlLink(res.custom.data);
                    }
                }
                handleNewContent();
            });
        }
        handleNewContent();
        $(".usrInput").focus();
    }, fadeTimeout);
}

// Suggestion and button functions
function addSuggestion(suggestions) {
    const suggLength = suggestions.length;
    const buttonsHtml = `
        <div class="singleCard">
            <div class="suggestions"><div class="menu"></div></div>
        </div>
    `;
    const $buttons = $(buttonsHtml)
        .appendTo(".chats")
        .hide()
        .fadeIn(100);

    for (let i = 0; i < suggLength; i += 1) {
        $(`<div class="menuChips" data-payload='${suggestions[i].payload}'>${suggestions[i].title}</div>`)
            .appendTo($buttons.find('.menu'));
    }
    handleNewContent();
}

function showButtons(buttonsData) {
    const { text, type, buttons } = buttonsData;

    if (type === 'quickrepliesbuttons') {
        showQuickReplies(buttonsData);
        return;
    }

    const botResponse = `
        <div class="botAvatar">
            <div class="botAvatar-image">
                <img src="./static/img/disha.svg"/>
            </div>
            <p class="botMsg">${text}</p>
        </div>
        <div class="clearfix"></div>
    `;
    $(botResponse).appendTo(".chats").hide().fadeIn(500);

    const buttonsHtml = `
        <div class="singleCard">
            <div class="suggestions"><div class="menu"></div></div>
        </div>
    `;
    const $buttons = $(buttonsHtml)
        .appendTo(".chats")
        .hide()
        .fadeIn(500);

    buttons.forEach(button => {
        let buttonHtml;
        if (button.type === 'urlLink') {
            buttonHtml = `<div class="menuChips urlLink" data-url="${button.url}">${button.title}</div>`;
        } else {
            buttonHtml = `<div class="menuChips" data-payload='${button.payload}'>${button.title}</div>`;
        }
        $(buttonHtml).appendTo($buttons.find('.menu'));
    });
    handleNewContent();
}

function showQuickReplies(quickRepliesData) {
    const { text, buttons } = quickRepliesData;

    const botResponse = `
        <div class="botAvatar">
            <div class="botAvatar-image">
                <img src="./static/img/disha.svg"/>
            </div>
            <p class="botMsg">${text}</p>
        </div>
        <div class="clearfix"></div>
    `;
    $(botResponse).appendTo(".chats").hide().fadeIn(500);

    const quickRepliesHtml = `
        <div class="quickReplies">
            <div class="quickRepliesMenu"></div>
        </div>
    `;
    const $quickReplies = $(quickRepliesHtml)
        .appendTo(".chats")
        .hide()
        .fadeIn(500);

    buttons.forEach(button => {
        const buttonHtml = `<div class="chipButton" data-payload='${button.payload}'>${button.title}</div>`;
        $(buttonHtml).appendTo($quickReplies.find('.quickRepliesMenu'));
    });
    handleNewContent();
}

function showUrlLink(urlLinkData) {
    const linkButtonsHtml = `
        <div class="singleCard">
            <div class="suggestions"><div class="menu"></div></div>
        </div>
    `;
    const $linkButtons = $(linkButtonsHtml)
        .appendTo(".chats")
        .hide()
        .fadeIn(100);

    urlLinkData.forEach(link => {
        $(`<div class="menuChips urlLink">
            <a href="${link.url}" target="_blank" rel="noopener noreferrer">
                ${link.title}
            </a>
        </div>`).appendTo($linkButtons.find('.menu'));
    });
    handleNewContent();
}

// Send message function
async function send(message) {
    await new Promise((r) => setTimeout(r, 2000));
    $.ajax({
        url: rasa_server_url,
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({message, sender: sender_id}),
        success(botResponse, status) {
            console.log("Response from Rasa: ", botResponse, "\nStatus: ", status);
            if (message.toLowerCase() === "/restart") {
                $("#userInput").prop("disabled", false);
                return;
            }
            setBotResponse(botResponse);
        },
        error(xhr, textStatus) {
            if (message.toLowerCase() === "/restart") {
                $("#userInput").prop("disabled", false);
            }
            setBotResponse("");
            console.log("Error from bot end: ", textStatus);
        },
    });
}

// Restart conversation function
function restartConversation() {
    $("#userInput").prop("disabled", true);
    $(".collapsible").remove();
    if (typeof chatChart !== "undefined") {
        chatChart.destroy();
    }
    $(".chart-container").remove();
    if (typeof modalChart !== "undefined") {
        modalChart.destroy();
    }
    $(".chats").html("");
    $(".usrInput").val("");
    send("/restart");
}

// Event listeners
$("#restart").click(() => {
    restartConversation();
});

$(".usrInput").on("keyup keypress", (e) => {
    const keyCode = e.keyCode || e.which;
    const text = $(".usrInput").val();
    if (keyCode === 13) {
        if (text === "" || $.trim(text) === "") {
            e.preventDefault();
            return false;
        }
        $(".collapsible").remove();
        $(".dropDownMsg").remove();
        $("#paginated_cards").remove();
        $(".quickReplies").remove();
        $(".usrInput").blur();
        setUserResponse(text);
        send(text);
        e.preventDefault();
        return false;
    }
    return true;
});

$("#sendButton").on("click", (e) => {
    const text = $(".usrInput").val();
    if (text === "" || $.trim(text) === "") {
        e.preventDefault();
        return false;
    }
    $(".collapsible").remove();
    $(".dropDownMsg").remove();
    $("#paginated_cards").remove();
    $(".quickReplies").remove();
    $(".usrInput").blur();
    setUserResponse(text);
    send(text);
    e.preventDefault();
    return false;
});

$(document).on("click", ".menu .menuChips", function () {
    const text = this.innerText;
    const payload = this.getAttribute("data-payload");
    console.log("payload: ", payload);
    setUserResponse(text);
    send(payload);
});

$(document).on("click", ".menu .urlLink", function (e) {
    e.preventDefault();
    const url = this.getAttribute("data-url");
    window.open(url, "_blank");
});

$(document).on("click", ".quickReplies .chipButton", function () {
    const text = this.innerText;
    const payload = this.getAttribute("data-payload");
    console.log("payload: ", payload);
    setUserResponse(text);
    send(payload);
});

// Scroll event listener
$("#chats").on("scroll", function() {
    isNearBottom = isUserNearBottom();
});

// Call this function when your chat interface is initialized
$(document).ready(function() {
    // Remove any existing event listeners
    $(".usrInput").off("keyup keypress");
    $("#sendButton").off("click");
    $(document).off("click", ".menu .menuChips");
    $(document).off("click", ".menu .urlLink");
    $(document).off("click", ".quickReplies .chipButton");

    // Reattach event listeners
    $(".usrInput").on("keyup keypress", function(e) {
        const keyCode = e.keyCode || e.which;
        const text = $(this).val();
        if (keyCode === 13) {
            if (text === "" || $.trim(text) === "") {
                e.preventDefault();
                return false;
            }
            $(".collapsible").remove();
            $(".dropDownMsg").remove();
            $("#paginated_cards").remove();
            $(".quickReplies").remove();
            $(this).blur();
            setUserResponse(text);
            send(text);
            e.preventDefault();
            return false;
        }
        return true;
    });

    $("#sendButton").on("click", function(e) {
        const text = $(".usrInput").val();
        if (text === "" || $.trim(text) === "") {
            e.preventDefault();
            return false;
        }
        $(".collapsible").remove();
        $(".dropDownMsg").remove();
        $("#paginated_cards").remove();
        $(".quickReplies").remove();
        $(".usrInput").blur();
        setUserResponse(text);
        send(text);
        e.preventDefault();
        return false;
    });

    $(document).on("click", ".menu .menuChips", function() {
        const text = this.innerText;
        const payload = this.getAttribute("data-payload");
        console.log("payload: ", payload);
        setUserResponse(text);
        send(payload);
    });

    $(document).on("click", ".menu .urlLink", function(e) {
        e.preventDefault();
        const url = this.getAttribute("data-url");
        window.open(url, "_blank");
    });

    $(document).on("click", ".quickReplies .chipButton", function() {
        const text = this.innerText;
        const payload = this.getAttribute("data-payload");
        console.log("payload: ", payload);
        setUserResponse(text);
        send(payload);
    });

    // Initialization
    updateChatScroll();
});
