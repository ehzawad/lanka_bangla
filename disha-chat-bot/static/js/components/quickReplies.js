
// ehzawad
function showQuickReplies(quickRepliesData) {
    let chips = "";
    for (let i = 0; i < quickRepliesData.length; i += 1) {
        const chip = `<div class="chip" data-payload='${quickRepliesData[i].payload}'>${quickRepliesData[i].title}</div>`;
        chips += chip;
    }

    const quickReplies = `<div class="quickReplies">${chips}</div><div class="clearfix"></div>`;
    $(quickReplies).appendTo(".chats").fadeIn(1000);
    scrollToBottomOfResults();

    const slider = document.querySelector(".quickReplies");
    let isDown = false;
    let startX;
    let scrollLeft;

    slider.addEventListener("mousedown", (e) => {
        isDown = true;
        slider.classList.add("active");
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
    });

    slider.addEventListener("mouseleave", () => {
        isDown = false;
        slider.classList.remove("active");
    });

    slider.addEventListener("mouseup", () => {
        isDown = false;
        slider.classList.remove("active");
    });

    slider.addEventListener("mousemove", (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX) * 2; // Adjusted scroll speed
        slider.scrollLeft = scrollLeft - walk;
    });

    // Add touch events for mobile devices
    slider.addEventListener("touchstart", (e) => {
        isDown = true;
        slider.classList.add("active");
        startX = e.touches[0].pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
    });

    slider.addEventListener("touchend", () => {
        isDown = false;
        slider.classList.remove("active");
    });

    slider.addEventListener("touchmove", (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.touches[0].pageX - slider.offsetLeft;
        const walk = (x - startX) * 2;
        slider.scrollLeft = scrollLeft - walk;
    });
}

// on click of quickreplies, get the payload value and send it to rasa
$(document).on("click", ".quickReplies .chip", function () {
    const text = this.innerText;
    const payload = this.getAttribute("data-payload");
    console.log("chip payload: ", this.getAttribute("data-payload"));
    setUserResponse(text);
    send(payload);

    // delete the quickreplies
    $(".quickReplies").remove();
});

