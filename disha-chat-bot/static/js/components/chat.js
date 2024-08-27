/**
 * scroll to the bottom of the chats after new message has been added to chat
 */
const converter = new showdown.Converter();

function scrollToBottomOfResults() {
    const terminalResultsDiv = document.getElementById("chats");
    terminalResultsDiv.scrollTop = terminalResultsDiv.scrollHeight;
}

/**
 * Set user response on the chat screen
 * @param {String} message user message
 */
function setUserResponse(message) {
    const user_response = `
<div class="userAvatar">
<div class="userAvatar-image">
    <img src='./static/img/userAvatar.png'>
</div>
<p class="userMsg">${message} </p>
</div>
<div class="clearfix"></div>
`;
    $(user_response).appendTo(".chats").show("slow");

    $(".usrInput").val("");
    scrollToBottomOfResults();
    showBotTyping();
    $(".suggestions").remove();
}

/**
 * returns formatted bot response
 * @param {String} text bot message response's text
 *
 */
function getBotResponse(text) {
    botResponse = `<img class="botAvatar" src="./static/img/bot-ai-logo.png"/><span class="botMsg">${text}</span><div class="clearfix"></div>`;
    return botResponse;
}
            




// zawad
function setBotResponse(response) {
    console.log("setBotResponse called with response:", response);
    setTimeout(() => {
        hideBotTyping();
        if (response.length < 1) {
            console.log("Empty response, displaying fallback message");
            const fallbackMsg = "I am facing some issues, please try again later!!!";
            const BotResponse = `
                <div class="botAvatar">
                    <div class="botAvatar-image">
                        <img src="./static/img/disha.svg"/>
                    </div>
                    <p class="botMsg">${fallbackMsg}</p>
                </div>
                <div class="clearfix"></div>`;
            $(BotResponse).appendTo(".chats").hide().fadeIn(1000);
            scrollToBottomOfResults();
        } else {
            console.log("Processing bot response");
            for (let i = 0; i < response.length; i += 1) {
                console.log(`Processing response item ${i}:`, response[i]);

                if (response[i].custom) {
                    console.log("Custom payload detected:", response[i].custom);
                }

                if (Object.hasOwnProperty.call(response[i], "text")) {
                    console.log("Text response detected:", response[i].text);
                    if (response[i].text != null) {
                        let botResponse;
                        let html = converter.makeHtml(response[i].text);
                        html = html
                            .replaceAll("<p>", "")
                            .replaceAll("</p>", "")
                            .replaceAll("<strong>", "<b>")
                            .replaceAll("</strong>", "</b>");
                        html = html.replace(/(?:\r\n|\r|\n)/g, "<br>");
                        console.log("Processed HTML:", html);

                        if (html.includes("<blockquote>")) {
                            html = html.replaceAll("<br>", "");
                            botResponse = getBotResponse(html);
                        } else if (html.includes("<img")) {
                            html = html.replaceAll("<img", '<img class="imgcard_mrkdwn" ');
                            botResponse = getBotResponse(html);
                        } else if (html.includes("<pre") || html.includes("<code>")) {
                            botResponse = getBotResponse(html);
                        } else if (
                            html.includes("<ul") ||
                            html.includes("<ol") ||
                            html.includes("<li") ||
                            html.includes("<h3")
                        ) {
                            html = html.replaceAll("<br>", "");
                            botResponse = getBotResponse(html);
                        } else {
                            botResponse = `
                                <div class="botAvatar">
                                    <div class="botAvatar-image">
                                        <img src="./static/img/disha.svg"/>
                                    </div>
                                    <p class="botMsg">${response[i].text}</p>
                                </div>
                                <div class="clearfix"></div>
                            `;
                        }
                        console.log("Appending bot response to chat");
                        $(botResponse).appendTo(".chats").hide().fadeIn(1000);
                    }
                }

                if (Object.hasOwnProperty.call(response[i], "image")) {
                    console.log("Image response detected:", response[i].image);
                    if (response[i].image !== null) {
                        const BotResponse = `<div class="singleCard"><img class="imgcard" src="${response[i].image}"></div><div class="clearfix">`;
                        $(BotResponse).appendTo(".chats").hide().fadeIn(1000);
                    }
                }

                if (Object.hasOwnProperty.call(response[i], "buttons")) {
                    console.log("Buttons detected:", response[i].buttons);
                    if (response[i].buttons.length > 0) {
                        console.log("Calling addSuggestion with buttons:", response[i].buttons);
                        addSuggestion(response[i].buttons);
                    }
                }

                if (Object.hasOwnProperty.call(response[i], "custom")) {
                    const {payload} = response[i].custom;
                    console.log("Custom payload type:", payload);
                    if (payload === "quickReplies") {
                        console.log("Quick replies detected:", response[i].custom.data);
                        const quickRepliesData = response[i].custom.data;
                        showQuickReplies(quickRepliesData);
                    } else if (payload === "buttonsPayload") {
                        console.log("Buttons payload detected:", response[i].custom.data);
                        const { text, buttons } = response[i].custom.data;
                        const botResponse = `
                            <div class="botAvatar">
                                <div class="botAvatar-image">
                                    <img src="./static/img/disha.svg"/>
                                </div>
                                <p class="botMsg">${text}</p>
                            </div>
                            <div class="clearfix"></div>
                        `;
                        $(botResponse).appendTo(".chats").hide().fadeIn(1000);
                        addSuggestion(buttons);
                    } else if (payload === "pdf_attachment") {
                        console.log("PDF attachment detected");
                        renderPdfAttachment(response[i]);
                    } else if (payload === "dropDown") {
                        console.log("Dropdown detected");
                        const dropDownData = response[i].custom.data;
                        renderDropDwon(dropDownData);
                    } else if (payload === "location") {
                        console.log("Location request detected");
                        $("#userInput").prop("disabled", true);
                        getLocation();
                    } else if (payload === "cardsCarousel") {
                        console.log("Cards carousel detected");
                        const restaurantsData = response[i].custom.data;
                        showCardsCarousel(restaurantsData);
                    } else if (payload === "chart") {
                        console.log("Chart detected");
                        const chartData = response[i].custom.data;
                        createChart(
                            chartData.title,
                            chartData.labels,
                            chartData.backgroundColor,
                            chartData.chartsData,
                            chartData.chartType,
                            chartData.displayLegend
                        );
                    } else if (payload === "collapsible") {
                        console.log("Collapsible detected");
                        createCollapsible(response[i].custom.data);
                    }
                }
                
                console.log("Scrolling to bottom of results");
                scrollToBottomOfResults();
            }
        }
        console.log("Setting focus to user input");
        $(".usrInput").focus();
    }, 500);
}


/**
 * sends the user message to the rasa server,
 * @param {String} message user message
 */
async function send(message) {
    await new Promise((r) => setTimeout(r, 2000));
    $.ajax({
        url: rasa_server_url,
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({message, sender: sender_id}),
        success(botResponse, status) {
            console.log("Response from Rasa: ", botResponse, "\nStatus: ", status);

            // if user wants to restart the chat and clear the existing chat contents
            if (message.toLowerCase() === "/restart") {
                $("#userInput").prop("disabled", false);

                // if you want the bot to start the conversation after restart
                // customActionTrigger();
                return;
            }
            setBotResponse(botResponse);
        },
        error(xhr, textStatus) {
            if (message.toLowerCase() === "/restart") {
                $("#userInput").prop("disabled", false);
                // if you want the bot to start the conversation after the restart action.
                // actionTrigger();
                // return;
            }

            // if there is no response from rasa server, set error bot response
            setBotResponse("");
            console.log("Error from bot end: ", textStatus);
        },
    });
}

/**
 * sends an event to the bot,
 *  so that bot can start the conversation by greeting the user
 *
 * `Note: this method will only work in Rasa 1.x`
 */
// eslint-disable-next-line no-unused-vars
function actionTrigger() {
    $.ajax({
        url: `http://localhost:5005/conversations/${sender_id}/execute`,
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            name: action_name,
            policy: "MappingPolicy",
            confidence: "0.98",
        }),
        success(botResponse, status) {
            console.log("Response from Rasa: ", botResponse, "\nStatus: ", status);

            if (Object.hasOwnProperty.call(botResponse, "messages")) {
                setBotResponse(botResponse.messages);
            }
            $("#userInput").prop("disabled", false);
        },
        error(xhr, textStatus) {
            // if there is no response from rasa server
            setBotResponse("");
            console.log("Error from bot end: ", textStatus);
            $("#userInput").prop("disabled", false);
        },
    });
}

/**
 * sends an event to the custom action server,
 *  so that bot can start the conversation by greeting the user
 *
 * Make sure you run action server using the command
 * `rasa run actions --cors "*"`
 *
 * `Note: this method will only work in Rasa 2.x`
 */
// eslint-disable-next-line no-unused-vars
function customActionTrigger() {
    $.ajax({
        url: "http://localhost:5055/webhook/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            next_action: action_name,
            tracker: {
                sender_id,
            },
        }),
        success(botResponse, status) {
            console.log("Response from Rasa: ", botResponse, "\nStatus: ", status);

            if (Object.hasOwnProperty.call(botResponse, "responses")) {
                setBotResponse(botResponse.responses);
            }
            $("#userInput").prop("disabled", false);
        },
        error(xhr, textStatus) {
            // if there is no response from rasa server
            setBotResponse("");
            console.log("Error from bot end: ", textStatus);
            $("#userInput").prop("disabled", false);
        },
    });
}

/**
 * clears the conversation from the chat screen
 * & sends the `/resart` event to the Rasa server
 */
function restartConversation() {
    $("#userInput").prop("disabled", true);
    // destroy the existing chart
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

// triggers restartConversation function.
$("#restart").click(() => {
    restartConversation();
});

/**
 * if user hits enter or send button
 * */
$(".usrInput").on("keyup keypress", (e) => {
    const keyCode = e.keyCode || e.which;

    const text = $(".usrInput").val();
    if (keyCode === 13) {
        if (text === "" || $.trim(text) === "") {
            e.preventDefault();
            return false;
        }
        // destroy the existing chart, if yu are not using charts, then comment the below lines
        $(".collapsible").remove();
        $(".dropDownMsg").remove();
        if (typeof chatChart !== "undefined") {
            chatChart.destroy();
        }

        $(".chart-container").remove();
        if (typeof modalChart !== "undefined") {
            modalChart.destroy();
        }

        $("#paginated_cards").remove();
        $(".suggestions").remove();
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
    // destroy the existing chart
    if (typeof chatChart !== "undefined") {
        chatChart.destroy();
    }

    $(".chart-container").remove();
    if (typeof modalChart !== "undefined") {
        modalChart.destroy();
    }

    $(".suggestions").remove();
    $("#paginated_cards").remove();
    $(".quickReplies").remove();
    $(".usrInput").blur();
    $(".dropDownMsg").remove();
    setUserResponse(text);
    send(text);
    e.preventDefault();
    return false;
});
