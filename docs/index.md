---
title: Home
layout: page 
---

# Vehicle Image Recognizer

Welcome to the Vehicle Image Recognizer, a powerful system capable of classifying various vehicles. Below is a list of vehicles it can identify:

<div class="vehicle-names">
  <p class="vehicle-name" data-name="car">car</p>
  <p class="vehicle-name" data-name="motorcycle">motorcycle</p>
  <p class="vehicle-name" data-name="bicycle">bicycle</p>
  <p class="vehicle-name" data-name="truck">truck</p>
  <p class="vehicle-name" data-name="bus">bus</p>
  <p class="vehicle-name" data-name="van">van</p>
  <p class="vehicle-name" data-name="rickshaw">rickshaw</p>
  <p class="vehicle-name" data-name="scooter">scooter</p>
  <p class="vehicle-name" data-name="skateboard">skateboard</p>
  <p class="vehicle-name" data-name="ambulance">ambulance</p>
  <p class="vehicle-name" data-name="fire truck">fire truck</p>
  <p class="vehicle-name" data-name="tractor">tractor</p>
  <p class="vehicle-name" data-name="segway">segway</p>
  <p class="vehicle-name" data-name="unicycle">unicycle</p>
  <p class="vehicle-name" data-name="jet ski">jet ski</p>
  <p class="vehicle-name" data-name="helicopter">helicopter</p>
  <p class="vehicle-name" data-name="airplane">airplane</p>
  <p class="vehicle-name" data-name="boat">boat</p>
  <p class="vehicle-name" data-name="kayak">kayak</p>
  <p class="vehicle-name" data-name="hovercraft">hovercraft</p>
</div>

<div id="vehicle-content" class="content">
  <!-- Content for the selected vehicle will appear here -->
</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    var vehicleNames = document.querySelectorAll(".vehicle-name");
    var contentDiv = document.getElementById("vehicle-content");

    vehicleNames.forEach(function (name) {
      name.addEventListener("click", function () {
        var vehicleName = this.getAttribute("data-name");
        contentDiv.innerHTML = getDescriptionBasedOnName(vehicleName);
        updateBackgroundColorBasedOnName(vehicleName);
      });
    });

    function getDescriptionBasedOnName(name) {
      // Define descriptions for each vehicle
      var descriptions = {
        car: "Cars are widely used for personal transportation.",
        motorcycle: "Motorcycles are popular for their agility and speed.",
        bicycle: "Bicycles are a healthy and eco-friendly mode of transportation.",
        truck: "Trucks are often used for transporting goods over long distances.",
        bus: "Buses are a common form of public transportation.",
        van: "Vans are versatile vehicles used for various purposes.",
        rickshaw: "Rickshaws are small, human-powered vehicles used in some regions.",
        scooter: "Scooters are compact and efficient for urban commuting.",
        skateboard: "Skateboards are recreational and a popular means of transportation for some.",
        ambulance: "Ambulances are specialized vehicles for medical emergencies.",
        "fire truck": "Fire trucks are equipped to handle firefighting and rescue operations.",
        tractor: "Tractors are used in agriculture for various tasks.",
        segway: "Segways are personal transportation devices with self-balancing technology.",
        unicycle: "Unicycles are a single-wheeled form of transportation.",
        "jet ski": "Jet skis are personal watercraft used for recreation on water.",
        helicopter: "Helicopters can hover and are used for various purposes, including transportation and rescue.",
        airplane: "Airplanes are a common mode of long-distance transportation.",
        boat: "Boats are vessels used for travel over water.",
        kayak: "Kayaks are small, narrow watercraft often used for recreation.",
        hovercraft: "Hovercraft can travel over land and water, using a cushion of air.",
      };

      return descriptions[name] || "Description not available for " + name + ".";
    }

    function updateBackgroundColorBasedOnName(name) {
      // Define background color based on the vehicle name
      var colors = {
        car: "#FFD700", // Gold
        motorcycle: "#FF4500", // OrangeRed
        // Add colors for other vehicles as needed
      };

      contentDiv.style.backgroundColor = colors[name] || "#FFFFFF"; // Default to white if color not defined
    }
  });
</script>

Feel free to test the recognition capabilities of our system by clicking on the vehicle names.
