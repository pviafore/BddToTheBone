"use strict";

$(document).ready(() => {
    bindButtonsToActions();
    loadStats();
});

function bindButtonsToActions() {
    $("#get-short-link").on("click", sendShortenRequest);
}

function sendShortenRequest() {
    const textInput = $("#input").val()
    if (textInput !== "") {
        $.ajax({
            url: "/createShortenedLink",
            method: "post",
            data: { url: textInput },
            dataType: "json",
            success: displayLink
        });
    }
}

function displayLink(data) {
    $("#return-link").text("Your new link is: " + data.shortened_link)
}

function loadStats() {
    $.ajax({
        url: "/get-stats",
        dataType: "json",
        success: displayStats
    });
}

function displayStats(data) {
    for (const url in data) {
        if (data.hasOwnProperty(url)) {
            const redirects = data[url];
            $("#stats").append("<tr><td>" + url + "</td><td>" + redirects + "</td></tr>")
        }
    }
}