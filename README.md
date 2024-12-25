# Santa's Workshop Project

This Django project helps Santa manage the Christmas toy delivery process, calculate production time, and generate statistics based on the kids' gift wishes, niceness, and delivery requirements.

## Endpoints can be accessed only by santa
- **username** - santa
- **password** - hohoho123!

## Endpoints

### 1. `/admin/`

- **Method**: `GET`
- **Description**: Access the Django admin panel to manage models, including `Kid`, `Toy`, and `SantasList`.

### 2. `/statistics/`

- **Method**: `GET`
- **Description**: This endpoint returns statistics about Santa's lists. It includes name of the list and number of nice/naughty kids in that particular list.
  
  **Response:**
  ```json
  {
    "lists": [
      {
        "list_name": "Christmas 2024",
        "nice_kids_count": 17,
        "naughty_kids_count": 13
      }
    ]
  }

### 3. `/statistics/toys/`

- **Method**: `GET`
- **Description**: This endpoint returns statistics about the toys needed based on kids' gift wishes and their niceness. It includes the overall production time, toy count, and delivery time.
  
  **Response:**
  ```json
  {
    "toys_needed": [
      {
        "name": "Teddy Bear",
        "required_quantity": 2,
        "total_production_time": 10
      }
    ],
    "overall_production_time": 10,
    "overall_toy_count": 2,
    "naughty_kids_count": 1,
    "total_delivery_time": 4.5,
    "total_needed_time": 14.5
  }

### 4. `/santa-list/`

- **Method**: `GET`
  - **Description**: This endpoint returns info about the kids with their wishes and their niceness.
  
    **Response:**
    ```json
    {
      "kids": [
        {
          "name": "Saba",
          "gift": "Horse",
          "niceness_coefficient": 10
        },
        {
          "name": "Mancho",
          "gift": "Car",
          "niceness_coefficient": 6
        },
      ]
    }
    
- **Method**: `POST`
- **Description**: This endpoint created info about new Kid. 
  
### 5. `/santa-list/nice/`

- **Method**: `GET`
  - **Description**: This endpoint returns info about nice kids with their wishes and their niceness.
  
    **Response:**
    ```json
    {
      "kids": [
        {
          "name": "Saba",
          "gift": "Horse",
          "niceness_coefficient": 10
        },
        {
          "name": "Mancho",
          "gift": "Car",
          "niceness_coefficient": 9
        },
      ]
    }

### 6. `/santa-list/naughty/`

- **Method**: `GET`
  - **Description**: This endpoint returns info about naughty kids with their wishes and their niceness.
  
    **Response:**
    ```json
    {
      "kids": [
        {
          "name": "Nana",
          "gift": "Lego",
          "niceness_coefficient": 2
        },
        {
          "name": "Nana",
          "gift": "Puzzle",
          "niceness_coefficient": 5
        },
      ]
    }