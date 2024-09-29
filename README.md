
# Smart Home Energy Management System (SHEMS)

## Project Vision

The **Smart Home Energy Management System (SHEMS)** is designed to help homeowners efficiently manage their energy consumption and reduce electricity bills. Integrating with various smart devices (such as washers, refrigerators, and lights), SHEMS provides users with detailed insights and control over their energy usage. The application stores past energy data, enabling users to make informed decisions on how to optimize their energy consumption based on appliance usage and settings.

## Features

### User Management
- **New User Registration & Login**: Users can sign up and securely log in to the SHEMS application.
- **Profile Management**: Users can edit their profile information (first name, last name, email) or delete their account.

### Service Locations & Device Management
- **Add/Edit Service Locations**: Users can add multiple service locations with details like address, square footage, and occupancy. Service locations can also be edited or deleted.
- **Device Enrollment & Management**: Users can add smart devices to each location by selecting a device type and model. Devices can be enrolled, viewed, and unenrolled as needed.

### Energy Usage & Visualization
- **Data Monitoring**: Devices continuously send data on events (on/off status, settings changes) and energy consumption to the system.
- **Visualizations with Chart.js**: Real-time visualizations for energy consumption are provided:
  - **Device-Level Insights**: View individual device energy usage and cumulative consumption.
  - **Service Location Analysis**: Monitor energy consumption across service locations with aggregated and detailed breakdowns.
  - **User Consumption Overview**: Analyze overall energy usage across all locations.

## Project Implementation

### 1. Database Design
The database schema supports multiple service locations for each user, each location having its own set of smart devices. Key entities include:
- **Customer**: Stores user details.
- **ServiceLocation**: Records information about each user's locations.
- **DeviceModel & EnrolledDevice**: Contains information about smart devices and their models.
- **EnergyPrice**: Logs energy prices by ZIP code and timestamp.
- **ModelEvent & Notification**: Tracks device events and notifies users of changes in device status.

<img width="452" alt="image" src="https://github.com/user-attachments/assets/77fd49ba-2d78-42fb-a35e-d3a29e7e0f40">

#### Assumptions:
- Events are recorded hourly, and energy prices update based on ZIP code on an hourly basis.
- Metrics for events like temperature (Celsius) and energy usage (Watt/hour) are standardized.

### 2. Technology Stack

- **Frontend Development**: The UI is built using **HTML, CSS, JavaScript**, with responsive design principles for optimal usability across devices. Data visualizations are powered by **Chart.js**.
- **Backend Development**: The server-side logic and data management are handled using the **Django framework**.
- **Database**: The system uses **PostgreSQL** for storing and retrieving data efficiently, leveraging its robust indexing and full-text search capabilities.

### 3. CI/CD Pipeline
A **Continuous Integration/Continuous Deployment (CI/CD) pipeline** was set up using **Travis CI**:
- **Black** for code formatting.
- **Flake8** for linting.
- **Coverage** for unit testing.
Achieved **96% test coverage**, ensuring robust and quality code.

## Schema Details

### Entities & Relationships
- **Customer Table**: Manages customer details (Primary Key: `CustomerID`).
- **ServiceLocation Table**: Tracks locations and relates to customers (Primary Key: `LocationID`).
- **DeviceModel & EnrolledDevice Tables**: Store device types, models, and their enrollment at locations.
- **EnergyPrice Table**: Contains energy cost data based on time and ZIP code.
- **ModelEvent & Notification Tables**: Log events per device and send alerts based on changes.

### Foreign Keys
- **CustomerID** references **ServiceLocation**.
- **LocationID** references **EnrolledDevice**.
- **ModelID** is associated with **DeviceModel** and **ModelEvent**.
- **EventID** ties to **Notification** and **ModelEvent**.

## Project Features

1. **Responsive User Interface**: Designed with a clean UI to allow users to easily register, log in, and navigate through the features.
2. **Profile & Device Management**: Intuitive forms to add/edit/delete service locations and devices.
3. **Real-Time Analytics & Visualization**: Visualizations provide insights into energy consumption, helping users make informed decisions to reduce electricity bills.
4. **Automated Code Quality Checks**: CI/CD setup ensures high code quality and seamless deployment.

## How to Run the Project
1. **Clone the Repository**: `git clone [repo-url]`
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Set Up Database**: Configure **PostgreSQL** and migrate the models: `python manage.py migrate`
4. **Run the Server**: `python manage.py runserver`
5. **Access the Application**: Navigate to `http://localhost:8000` in your browser.

## Conclusion

The Smart Home Energy Management System (SHEMS) brings smart energy control into the hands of homeowners, offering detailed usage data, insights, and management capabilities for their smart devices. By enabling efficient energy use, SHEMS empowers users to make cost-effective and eco-friendly decisions for their homes.
