const story = window.STORY_DATA;
const chapters = Array.isArray(story.chapters) ? story.chapters : [];

const panelLink = document.getElementById("panel-link");
const chapterCards = document.getElementById("chapter-cards");
const panelTitle = document.getElementById("panel-title");
const panelTime = document.getElementById("panel-time");
const panelSummary = document.getElementById("panel-summary");
const panelMedia = document.getElementById("panel-media");
const panelBody = document.getElementById("panel-body");
const playRouteButton = document.getElementById("play-route");
const fitRouteButton = document.getElementById("fit-route");

const map = L.map("map", {
    zoomControl: true,
    scrollWheelZoom: true
}).setView(story.map.center || [20, 0], story.map.zoom || 2);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution: "&copy; OpenStreetMap contributors"
}).addTo(map);

const routePoints = chapters
    .filter((chapter) => Array.isArray(chapter.coordinates) && chapter.coordinates.length === 2)
    .sort((a, b) => (a.order || 0) - (b.order || 0))
    .map((chapter) => chapter.coordinates);

const routeLine = routePoints.length >= 2
    ? L.polyline(routePoints, { weight: 4, opacity: 0.7 })
    : null;

if (routeLine) {
    routeLine.addTo(map);
}

const markerEntries = [];
let activeIndex = 0;
let playTimer = null;

function createMarkerIcon(active = false) {
    return L.divIcon({
        className: "",
        html: `<div class="custom-marker${active ? " active" : ""}"></div>`,
        iconSize: [18, 18],
        iconAnchor: [9, 9]
    });
}

function updateNarrative(chapter, index) {
    activeIndex = index;
    panelTitle.textContent = chapter.title || "Untitled chapter";
    panelTime.textContent = chapter.year || "";
    panelSummary.textContent = chapter.summary || "";

    panelMedia.innerHTML = chapter.image
        ? `<img src="${chapter.image}" alt="${chapter.title || "Story image"}">`
        : "";

    if (chapter.link_url) {
        panelLink.innerHTML = `
            <p>
                <a href="${chapter.link_url}" target="_blank" rel="noopener noreferrer">
                    ${chapter.link_title || "Open link"}
                </a>
            </p>
        `;
    } else {
        panelLink.innerHTML = "";
    }

    panelBody.innerHTML = Array.isArray(chapter.body)
        ? chapter.body.map((paragraph) => `<p>${paragraph}</p>`).join("")
        : "";

    document.querySelectorAll(".chapter-card").forEach((card, cardIndex) => {
        card.classList.toggle("active", cardIndex === index);
    });

    markerEntries.forEach((entry, markerIndex) => {
        entry.marker.setIcon(createMarkerIcon(markerIndex === index));
    });

    if (Array.isArray(chapter.coordinates) && chapter.coordinates.length === 2) {
        map.flyTo(chapter.coordinates, chapter.zoom || 6, {
            animate: true,
            duration: 1.25
        });
    }
}

function buildCards() {
    chapters.forEach((chapter, index) => {
        const button = document.createElement("button");
        button.type = "button";
        button.className = `chapter-card${index === 0 ? " active" : ""}`;
        button.innerHTML = `
            <div class="chapter-card-head">
                <h4>${chapter.title || "Untitled chapter"}</h4>
                <span class="year">${chapter.year || ""}</span>
            </div>
            <p>${chapter.summary || ""}</p>
            <span class="tag">${chapter.place || "Location"}</span>
        `;
        button.addEventListener("click", () => updateNarrative(chapter, index));
        chapterCards.appendChild(button);
    });
}

function buildMarkers() {
    chapters.forEach((chapter, index) => {
        if (!Array.isArray(chapter.coordinates) || chapter.coordinates.length !== 2) {
            return;
        }

        const marker = L.marker(chapter.coordinates, {
            icon: createMarkerIcon(index === 0)
        }).addTo(map);

        marker.bindPopup(`
            <strong>${chapter.title || "Untitled chapter"}</strong><br>
            ${chapter.place || ""}<br>
            ${chapter.year || ""}
        `);

        marker.on("click", () => updateNarrative(chapter, index));
        markerEntries.push({ marker, chapter, index });
    });
}

function fitAllPoints() {
    if (markerEntries.length === 0) {
        return;
    }

    const group = L.featureGroup(markerEntries.map((entry) => entry.marker));
    map.fitBounds(group.getBounds().pad(0.15));
}

function playRoute() {
    if (playTimer) {
        window.clearInterval(playTimer);
        playTimer = null;
        playRouteButton.textContent = "Play journey";
        return;
    }

    updateNarrative(chapters[0], 0);
    playRouteButton.textContent = "Stop journey";

    let current = 0;
    playTimer = window.setInterval(() => {
        current += 1;
        if (current >= chapters.length) {
            window.clearInterval(playTimer);
            playTimer = null;
            playRouteButton.textContent = "Play journey";
            return;
        }
        updateNarrative(chapters[current], current);
    }, 3500);
}

buildCards();
buildMarkers();

if (markerEntries.length > 1) {
    fitAllPoints();
} else if (chapters[0] && Array.isArray(chapters[0].coordinates)) {
    updateNarrative(chapters[0], 0);
}

playRouteButton.addEventListener("click", playRoute);
fitRouteButton.addEventListener("click", fitAllPoints);