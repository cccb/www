---
title: "Kalender"
subtitle: "Der Kalender des CCCB"
date: 2025-02-26T10:00:00+02:00
menu:
  main:
    parent: "verein"
---

<!-- Kalender-Widget -->
<style>
  .calendar-container {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    gap: 20px;
  }
  #calendar {
    flex: 1;
    min-width: 300px;
  }
  #event-panel {
    flex: 1;
    min-width: 300px;
    background-color: var(--color-bg-secondary);
    padding: 15px;
    border-radius: 5px;
    min-height: 300px;
    display: none;
  }
  #calendar-controls {
    text-align: center;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  #calendar-controls button {
    background: none;
    border: none;
    font-size: 2em;
    cursor: pointer;
    padding: 5px 15px;
  }
  #calendar-table {
    width: 100%;
    border-collapse: collapse;
  }
  #calendar-table th, #calendar-table td {
    border: 1px solid var(--color-border);
    padding: 5px;
    text-align: center;
    vertical-align: top;
    height: 60px;
    width: 14.28%;
  }
  #calendar-table th {
    background-color: var(--color-bg-secondary);
  }
  #calendar-table td {
    background-color: var(--color-bg-primary);
    position: relative;
    cursor: pointer;
  }
  #calendar-table td:hover {
    background-color: var(--color-bg-hover);
  }
  .event-dot {
    height: 8px;
    width: 8px;
    background-color: greenyellow;
    border-radius: 50%;
    display: block;
    margin: 5px auto 0;
  }
  .has-event {
    background-color: var(--color-bg-secondary) !important;
  }
  .selected-day {
    background-color: var(--color-bg-hover) !important;
    font-weight: bold;
  }
  #event-date {
    font-size: 1.2em;
    margin-bottom: 15px;
  }
  .event-item {
    margin-bottom: 15px;
    padding-bottom: 15px;
    border-bottom: 1px solid var(--color-border);
  }
  .event-title {
    font-weight: bold;
    margin-bottom: 5px;
  }
  .event-time, .event-description {
    font-size: 0.9em;
    margin-bottom: 5px;
  }
  .no-events {
    font-style: italic;
    color: var(--color-text-secondary);
  }
</style>

<div class="calendar-container">
  <div id="calendar">
    <div id="calendar-controls">
      <button id="prev-month">&larr;</button>
      <span id="current-month"></span>
      <button id="next-month">&rarr;</button>
    </div>
    <table id="calendar-table">
      <thead>
        <tr>
          <th>Mo</th>
          <th>Di</th>
          <th>Mi</th>
          <th>Do</th>
          <th>Fr</th>
          <th>Sa</th>
          <th>So</th>
        </tr>
      </thead>
      <tbody id="calendar-body"></tbody>
    </table>
  </div>
  <div id="event-panel">
    <div id="event-date"></div>
    <div id="event-details"></div>
  </div>
</div>

<script>
(function(){
    let events = [];
    let eventsByDate = {};

    // Funktion zum Parsen der ICS-Datei
    function parseICS(icsText) {
        let events = [];
        let lines = icsText.split(/\r?\n/);
        let event = null;
        lines.forEach(line => {
            if (line.startsWith("BEGIN:VEVENT")) {
                event = {};
            } else if (line.startsWith("END:VEVENT")) {
                if (event) events.push(event);
                event = null;
            } else if (event) {
                let colonIndex = line.indexOf(":");
                if (colonIndex > -1) {
                    let key = line.substring(0, colonIndex);
                    let value = line.substring(colonIndex + 1);
                    if (key.startsWith("DTSTART")) {
                        event.start = value;
                    } else if (key.startsWith("DTEND")) {
                        event.end = value;
                    } else if (key.startsWith("SUMMARY")) {
                        event.summary = value;
                    } else if (key.startsWith("DESCRIPTION")) {
                        event.description = value;
                    }
                }
            }
        });
        return events;
    }

    // Hilfsfunktion: Parst einen ICS-Datum-String ins Format "YYYY-MM-DD"
    function parseDateString(icsDateStr) {
        // Erwartet entweder ganztägige Daten (YYYYMMDD) oder Datum+Zeit (YYYYMMDDTHHmmssZ)
        if (icsDateStr.length === 8) {
            let year = icsDateStr.substring(0, 4);
            let month = icsDateStr.substring(4, 6);
            let day = icsDateStr.substring(6, 8);
            return `${year}-${month}-${day}`;
        } else if (icsDateStr.length >= 15) {
            let year = icsDateStr.substring(0, 4);
            let month = icsDateStr.substring(4, 6);
            let day = icsDateStr.substring(6, 8);
            return `${year}-${month}-${day}`;
        }
        return null;
    }

    // Kalender initialisieren
    let currentYear, currentMonth;
    const currentMonthElem = document.getElementById("current-month");
    const calendarBody = document.getElementById("calendar-body");
    const eventPanel = document.getElementById("event-panel");
    const eventDateElem = document.getElementById("event-date");
    const eventDetailsElem = document.getElementById("event-details");

    document.getElementById("prev-month").addEventListener("click", function(){
         currentMonth--;
         if (currentMonth < 0) {
              currentMonth = 11;
              currentYear--;
         }
         renderCalendar(currentYear, currentMonth);
    });
    document.getElementById("next-month").addEventListener("click", function(){
         currentMonth++;
         if (currentMonth > 11) {
              currentMonth = 0;
              currentYear++;
         }
         renderCalendar(currentYear, currentMonth);
    });

    function renderCalendar(year, month) {
        // Setze die Monatsbeschriftung (in Deutsch)
        const monthNames = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"];
        currentMonthElem.textContent = monthNames[month] + " " + year;
        calendarBody.innerHTML = "";

        let firstDay = new Date(year, month, 1);
        let firstDayIndex = (firstDay.getDay() + 6) % 7; // Montag = 0, Dienstag = 1, etc.
        let daysInMonth = new Date(year, month + 1, 0).getDate();

        let row = document.createElement("tr");
        // Leere Zellen vor dem 1. Tag
        for (let i = 0; i < firstDayIndex; i++){
            let cell = document.createElement("td");
            row.appendChild(cell);
        }

        // Tage hinzufügen
        for (let day = 1; day <= daysInMonth; day++){
            if (row.children.length === 7) {
                calendarBody.appendChild(row);
                row = document.createElement("tr");
            }
            let cell = document.createElement("td");
            cell.innerHTML = "<strong>" + day + "</strong>";
            
            let dayStr = day < 10 ? "0" + day : day;
            let monthStr = (month + 1) < 10 ? "0" + (month + 1) : (month + 1);
            let dateKey = year + "-" + monthStr + "-" + dayStr;
            
            if (eventsByDate[dateKey]) {
                let eventDot = document.createElement("div");
                eventDot.className = "event-dot";
                cell.appendChild(document.createElement("br"));
                cell.appendChild(eventDot);
                
                cell.dataset.dateKey = dateKey;
                cell.addEventListener("click", function() {
                    // Clear previous selections
                    document.querySelectorAll('.selected-day').forEach(el => {
                        el.classList.remove('selected-day');
                    });
                    cell.classList.add('selected-day');
                    showEventDetails(dateKey);
                });
            }
            row.appendChild(cell);
        }
        // Falls die letzte Zeile nicht komplett ist
        while (row.children.length < 7) {
            let cell = document.createElement("td");
            row.appendChild(cell);
        }
        calendarBody.appendChild(row);
    }

    function createEventLink(eventTitle) {
        if (eventTitle.startsWith("Datengarten")) {
            // Extract the number after "Datengarten "
            const match = eventTitle.match(/Datengarten\s+(\d+)/i);
            if (match && match[1]) {
                return `https://berlin.ccc.de/datengarten/${match[1]}/`;
            }
        } 
        
        // For other titles, convert to lowercase and use as path
        const slug = eventTitle.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]/g, '');
        return `https://berlin.ccc.de/page/${slug}/`;
    }

    function showEventDetails(dateKey) {
        const events = eventsByDate[dateKey];
        eventDateElem.textContent = formatDate(dateKey);
        eventDetailsElem.innerHTML = "";

        if (events && events.length > 0) {
            events.forEach(ev => {
                let eventItem = document.createElement("div");
                eventItem.className = "event-item";

                let eventTitle = document.createElement("div");
                eventTitle.className = "event-title";
                
                // Create a link for the event title
                let titleLink = document.createElement("a");
                titleLink.textContent = ev.summary;
                titleLink.href = createEventLink(ev.summary);
                titleLink.target = "_blank";
                eventTitle.appendChild(titleLink);
                
                eventItem.appendChild(eventTitle);

                let eventTime = document.createElement("div");
                eventTime.className = "event-time";
                eventTime.textContent = `Start: ${formatTime(ev.start)}, End: ${formatTime(ev.end)}`;
                eventItem.appendChild(eventTime);

                if (ev.description) {
                    let eventDescription = document.createElement("div");
                    eventDescription.className = "event-description";
                    eventDescription.textContent = ev.description;
                    eventItem.appendChild(eventDescription);
                }

                eventDetailsElem.appendChild(eventItem);
            });
        } else {
            let noEvents = document.createElement("div");
            noEvents.className = "no-events";
            noEvents.textContent = "Keine Veranstaltungen an diesem Tag.";
            eventDetailsElem.appendChild(noEvents);
        }

        eventPanel.style.display = "block";
    }

    function formatDate(dateStr) {
        // Convert YYYY-MM-DD to DD.MM.YYYY
        const parts = dateStr.split("-");
        return `${parts[2]}.${parts[1]}.${parts[0]}`;
    }

    function formatTime(icsTimeStr) {
        // Format time for display
        if (icsTimeStr.length === 8) {
            // All-day event
            return "Ganztägig";
        } else if (icsTimeStr.length >= 15) {
            // Time-specific event
            const hour = icsTimeStr.substring(9, 11);
            const minute = icsTimeStr.substring(11, 13);
            return `${hour}:${minute}`;
        }
        return icsTimeStr;
    }

    // ICS-Datei abrufen und Events verarbeiten
    fetch('/all.ics')
      .then(response => response.text())
      .then(data => {
         events = parseICS(data);
         events.forEach(ev => {
             let dateKey = parseDateString(ev.start);
             if (dateKey) {
                if (!eventsByDate[dateKey]) {
                    eventsByDate[dateKey] = [];
                }
                eventsByDate[dateKey].push(ev);
             }
         });
         let today = new Date();
         currentYear = today.getFullYear();
         currentMonth = today.getMonth();
         renderCalendar(currentYear, currentMonth);
      })
      .catch(err => console.error('Fehler beim Laden der ICS-Datei:', err));
})();
</script>
