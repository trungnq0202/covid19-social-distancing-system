import React, { useEffect, useState } from "react";
import Layout from "../../hoc/Layout/Layout";
import axios from "../../axios-request";
import "./QRCodeScan.css";
import { PersonCheckFill, PersonDashFill, PeopleFill } from "react-bootstrap-icons";
import waitImage from "./waiting.jpg";
const QRCodeScan = (props) => {
  const [imgSrc, setImgSrc] = useState({});
  const [peopleData, setPeopleData] = useState({});

  let streamingSrc = "http://172.20.10.90:8082/";

   // Fetch people data
  const fetchPeopleVariables = async () => {
    const res = await axios.get("/humanEntryAndExit/get/people");
    setPeopleData(res.data);
  };

  useEffect(() => {
    setInterval(() => {
        console.log(window.location.href);
        if (window.location.href == "http://localhost:3000/qr-code-scan"){
          checkStreamOn();
          fetchPeopleVariables();
        } 
    }, 2000);
}, []);

  const checkStreamOn = async () => {
    const res = await axios.get("http://0.0.0.0:8001/qrcode/getStatus");
    if (res.data == "pending") {
      setImgSrc(streamingSrc);
    } else {
      setImgSrc(waitImage);
    }
  };

  return (
    <Layout>
      <div className="row" style={{ height: "100vh" }}>
        <div className="container  text-center">
          <h1 className="text-center" style={{ padding: "20px" }}>
            QR Code Scanner
          </h1>
          <div
            id="qrCodeScan"
            className="container text-center"
            style={{ padding: "20px" }}
          >
            <img
              className="qr-scan-block"
              alt=" "
              src={imgSrc}
              width="300px"
              style={{
                display: "block",
                marginLeft: "auto",
                marginRight: "auto",
                paddingBottom: "5vh",
              }}
            ></img>
          </div>

          <div className="row text-center">

            <div class="col-md" style={{ padding: "10px" }}>
              <PeopleFill size={70} />
              <br />
              <h4> Number of people in the room </h4>
              <h4> {peopleData.current_num} </h4>
            </div>

            <div class="col-md" style={{ padding: "10px" }}>
              <PersonCheckFill size={70} />
              <br />
              <h4> Total number of people check in </h4>
              <h4> {peopleData.total_number_people_in} </h4>
            </div>

            <div class="col-md" style={{ padding: "10px" }}>
              <PersonDashFill size={70} />
              <br />
              <h4> Total number of people check out </h4>
              <h4> {peopleData.total_number_people_out} </h4>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default QRCodeScan;
