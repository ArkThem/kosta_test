## Таблица "Services"
В таблице "Services" содержится список всех услуг, предоставляемых поликлиникой. Она содержит следующие поля:

 - service_id (INTEGER) - уникальный идентификатор услуги;
 - service_name (VARCHAR) - название услуги;
 - service_description (VARCHAR) - описание услуги.

## Таблица "PriceList"
В таблице "PriceList" содержится информация о ценах на услуги на определенный период времени. Она содержит следующие поля:

 - price_id (INTEGER) - уникальный идентификатор записи о цене;
 - service_id (INTEGER) - идентификатор услуги, на которую устанавливается цена;
 - price (DECIMAL) - цена на услугу;
 - date_from (DATE) - дата, с которой начинается действие цены;
 - date_to (DATE) - дата, до которой действует цена.

С помощью SQLalchemy и Python были написаны функции для работы с базой данных. Были предоставлены примеры запросов для добавления новой услуги, получения списка услуг и их цен, обновления цены на услугу и удаления услуги и ее цен из базы данных.
