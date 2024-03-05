BIN_DIR := ../bin

all: build

build: simple_db simple_db_find not_simple_db

simple_db: db.c
	gcc -Werror -Wall -Wextra -std=c11 -o ${BIN_DIR}/simple_db db.c

simple_db_find: db.c
	gcc -Werror -Wall -Wextra -std=c11 -o ${BIN_DIR}/simple_db_find db.c

not_simple_db: db.c
	gcc -Werror -Wall -Wextra -std=c11 -o ${BIN_DIR}/not_simple_db db.c