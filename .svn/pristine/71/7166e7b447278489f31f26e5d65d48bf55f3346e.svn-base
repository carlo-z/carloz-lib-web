--CREATE DEFINER = CURRENT_USER FUNCTION `NewProc`(`p_str` varchar(1024),`p_split` varchar(10),`p_index` int)
CREATE FUNCTION `func_get_array_item_by_index`(`p_str` varchar(1024),`p_split` varchar(10),`p_index` int)
 RETURNS varchar(1024) CHARSET utf8
BEGIN
    DECLARE v_location int;
    DECLARE v_start int DEFAULT 1;
    DECLARE v_next int DEFAULT 1;
    DECLARE v_seed int DEFAULT LENGTH(p_split);

    SET p_str=TRIM(p_str);
    SET v_location = LOCATE(p_split, p_str);

    WHILE v_location<>0 AND p_index > v_next DO
        SET v_start = v_location + v_seed;
        SET v_location = LOCATE(p_split, p_str, v_start);
        SET v_next = v_next + 1;
    END WHILE;
    IF v_location =0 THEN
        SET v_location = LENGTH(p_str) + 1;
    END IF;

    RETURN SUBSTRING(p_str, v_start, v_location-v_start);
END;;


--func_get_array_item_by_index