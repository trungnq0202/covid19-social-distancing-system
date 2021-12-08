import { Container, Row, Col } from "react-bootstrap";
import Layout from "../../../hoc/Layout/Layout";

import "./NotFound.css";

const NotFound = () => {
  return (
    <Layout>
      <Container>
        <Row>
          <Col md={12} className="mx-auto mt-5">
            <div class="error-template">
              <h1>Oops!</h1>
              <h2>404 Not Found</h2>
              <div class="error-details">
                Sorry, an error has occured, Requested page not found!
              </div>
            </div>
          </Col>
        </Row>
      </Container>
    </Layout>
  );
};

export default NotFound;
