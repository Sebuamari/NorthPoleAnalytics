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

### 6. `/santa-list/{kid-id}/`

- **Method**: `GET`
  - **Description**: This endpoint returns info about the kid with ID specified in the URL.
  
    **Response:**
    ```json
    {
      "name": "Lasha",
      "niceness_coefficient": 9,
      "gift": "Puzzle",
      "santas_list": "Christmas 2024"
    }

### 6. `/toy_factory/`

  - **Method**: `DELETE`
  - **Description**: This endpoint removes kid from the list.

  - **Method**: `GET`
  - **Description**: This endpoint returns info about the kid with ID specified in the URL.
  
    **Response:**
    ```json
    {
      "toys": [
        {
          "name": "Horse",
          "toy_type": "Doll",
          "quantity": 6
        },
        {
          "name": "Ball",
          "toy_type": "Sports",
          "quantity": 1
        }
      ],
      "coals": [
        {
          "coals": 13
        }
      ]
    }

### 6. `/toy_factory/produce/`

  - **Method**: `POST`
  - **Description**: This endpoint produces toys and coals for children if they're needed.