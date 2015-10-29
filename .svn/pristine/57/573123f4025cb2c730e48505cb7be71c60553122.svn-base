CREATE FUNCTION `func_get_array_len`(`p_str` varchar(1024), `p_split` varchar(10))
 RETURNS int
BEGIN
    DECLARE v_location INT;
    DECLARE v_start INT;
    DECLARE v_length INT DEFAULT 1;

    SET p_str = TRIM(p_str);
    SET v_location = LOCATE(p_split,p_str);

    WHILE v_location <> 0 DO
        SET v_start = v_location+1;
        SET v_location = LOCATE(p_split, p_str, v_start);
        SET v_length = v_length+1;
    END WHILE;
    RETURN v_length;
END;;

--func_get_array_len
--CREATE DEFINER = CURRENT_USER FUNCTION `func_get_array_len`(`p_str` varchar(1024),`p_split` varchar(10))