import React, { useEffect, useState } from "react";
import Layout from "../../hoc/Layout/Layout";

const QRCodeScan = (props) => {
    
    return (
        <Layout>
            <div className="container">
                <h1 className="text-center">QR Code Scan</h1>
                <img src="http://192.168.0.101:6064/video-feed"></img>

            </div>
        </Layout>
    )
} 

export default QRCodeScan;