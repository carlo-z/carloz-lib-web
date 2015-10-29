--requirement: func_get_array_len && func_get_array_item_by_index first

--CREATE DEFINER = CURRENT_USER FUNCTION `NewProc`(`p_tag_id_list` varchar(1024))
CREATE FUNCTION `func_get_tag_list`(`p_tag_id_list` varchar(1024))
 RETURNS varchar(2048) CHARSET utf8
BEGIN
    DECLARE v_arr_len int DEFAULT func_get_array_len(p_tag_id_list, ',');
    DECLARE v_index int DEFAULT 1;
    DECLARE v_tag_list varchar(2048) DEFAULT '';
    DECLARE v_tag_id varchar(200);
    DECLARE v_tag_name varchar(200);
        
    WHILE v_index <= v_arr_len DO
        SET v_tag_id = func_get_array_item_by_index(p_tag_id_list, ',', v_index);
        IF v_tag_id IS NOT NULL AND v_tag_id != '' THEN
            SELECT t.tag_name INTO v_tag_name
            FROM t_tag t
            WHERE t.id = CAST(v_tag_id AS UNSIGNED INTEGER);
            IF v_tag_name IS NOT NULL AND v_tag_name != '' THEN
                SET v_tag_list = CONCAT(CONCAT(CONCAT(CONCAT(v_tag_list, v_tag_id), ':'), v_tag_name), ',');
            END IF;
      SET v_tag_name = '';
        END IF;
        SET v_index = v_index + 1;
    END WHILE;

    RETURN v_tag_list;
END;;

--func_get_tag_list