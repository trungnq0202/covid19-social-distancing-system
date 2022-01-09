import React, { useEffect, useState } from "react";
import Layout from "../../hoc/Layout/Layout";
import axios from "../../axios-request";
import "./HomePage.css";
import design3map from "./design3map.png";
const HomePage = (props) => {
  return (
    <Layout>
      <div className="container bg-light text-dark" style={{ padding: "11px" }}>
        <div className="container align-self-center" style={{ width: "100vw" }}>
          <h1 className="text-center"  style={{ padding: "20px" }}>Social distancing system</h1>

          <div>
            The project is to design and build an IoT system which would be used
            for Wuhan virus detection in a working environment. The technical
            group consists of six people, from different engineering majors
            (Robotics, Electrics and Softwares), who would implement the IoT
            system to perform certain tasks. The specification of the system is
            limited to the given hardware from RMIT lecturer (sensors, cameras,
            Raspberry Pi).
          </div>
          <div className="text-center" style={{ padding: "30px" }}>
            <img
              src={design3map}
              class="img-thumbnail img-fluid"
              alt="Hollywood Sign on The Hill"
            />
          </div>
        </div>

        <div
          className="row text-light bg-primary"
          style={{ padding: "30px", }}
        >
          <div className="col-md-6 align-self-center">
            <h3>Task 1: Human entry and exit detection</h3>
            <br></br>
            <p>
              The system of a camera accompanying an ultrasonic Sensor is used
              to detect people entering or exiting the room. to detect human
              action and define whether the human is entering the room or exit.
              To accomplish this, we use a set of 2 motion PIR sensors: one is
              outside the room and the other is inside. The sensor is triggered
              when there is a motion around the door and the order which sensor
              is triggered first will classify the action as entry or exit. When
              the system detects there is a person entering the room, the system
              will request the person to scan QR code and display the
              information to the LCD and web application.
            </p>
          </div>
          <div className="col-md-6 text-center">
            <img
              src="https://www.pyimagesearch.com/wp-content/uploads/2018/08/opencv_people_counter_featured.jpg"
              class="img-thumbnail img-fluid"
              alt=""
              width="400px"
            />
          </div>
        </div>

        <div className="row" style={{ padding: "30px" }}>
          <div className="col-md-6 text-center ">
            <img
              src="https://i.ytimg.com/vi/DPvxsHoD7kc/maxresdefault.jpg"
              class="img-thumbnail img-fluid"
              alt=""
              width="500px"
            />
          </div>
          <div className="col-md-6 align-self-center">
            <h3>Task 2: Room Environment Monitor</h3>
            <br />
            <p>
              We use the sensors for monitoring the room environment and detect
              the human entry and exit. For the former task, we use a humidity
              and temperature sensor to get the temperature and humidity each 10
              seconds and put it in the database.
            </p>
          </div>
        </div>

        <div className="row text-light bg-primary" style={{ padding: "30px" }}>
          <div className="col-md-6 align-self-center">
            <h3>Task 3: Safety Social Distance Monitoring</h3>
            <p>
              The acceptable distance between two people in the room is 1.5m.
              The camera is added so that if there is some violation of the
              policy, the notification will be sent to the user interface for
              the security to do something about it.
            </p>
          </div>
          <div className="col-md-6 text-center">
            <img
              src="https://www.ulethbridge.ca/sites/default/files/2020/09/2m_distancing.png"
              class="img-thumbnail img-fluid"
              alt=""
              width="400px"
            />
          </div>
        </div>

        <div className="row" style={{ padding: "30px" }}>
          <div className="col-md-6 text-center">
            <img
              src="https://groundup.ai/wp-content/uploads/2021/03/social_distance_detector_people_detections.jpg"
              class="img-thumbnail img-fluid"
              alt=""
              width="500px"
            />
          </div>
          <div className="col-md-6 align-self-center" >
            <h3>Task 4: Detection of People Assembly</h3>
            <p>
              A camera stream is added to detect human people in the room and
              highlight them in the UI. If the number of people gathering is
              higher than the maximum of 3, the notification will be sent to the
              user interface for the security to do something about it.
            </p>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default HomePage;
