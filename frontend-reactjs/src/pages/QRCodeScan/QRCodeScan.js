import React, { useEffect, useState } from "react";
import Layout from "../../hoc/Layout/Layout";
import axios from "../../axios-request";
import "./QRCodeScan.css";
import { PersonCheckFill, PersonDashFill } from "react-bootstrap-icons";

const QRCodeScan = (props) => {
  useEffect(() => {
    axios.get("http://172.20.10.6:6064/keep-alive");
  }, []);

  return (
    <Layout>
      <div className="row">
        <div className="container">
          <h1 className="text-center">QR Code Scan</h1>
          <img
            className="qr-scan-block"
            src="http://172.20.10.6:6064/video-feed"
          ></img>
        </div>

        <div className="row" style={{ padding: "20px" }}></div>
      </div>
    </Layout>
  );
};

export default QRCodeScan;
