import React, { useEffect, useState } from "react";
import Layout from "../../hoc/Layout/Layout";
import axios from "../../axios-request";
import './HomePage.css';

const HomePage = (props) => {
    return (
        <Layout>
            <div className="container ">
                <h1 className="text-center text-info">Social distancing system</h1>
            </div>
        </Layout>
    )
} 

export default HomePage;