{ pkgs ? import <nixpkgs> { } }:
with pkgs;
mkShell {
  buildInputs = [
    python39

    redis

    libmysqlclient
    pkg-config
    mysql

    # sqlite
    # mariadb


  ];

  shellHook = ''
    VENV_HOME="$PWD/venv"

    # init venv
    if [ ! -d "$VENV_HOME" ]; then
      # virtualenv venv
      python -m venv venv
    fi

    # source activate script
    . venv/bin/activate
  '';

  # start local mysql server when entering nix develop shell
  # https://jeancharles.quillet.org/posts/2022-01-30-Local-mariadb-server-with-nix-shell.html
  # + ''
  #   MYSQL_BASEDIR=${pkgs.mariadb}
  #   MYSQL_HOME=$PWD/.db
  #   MYSQL_DATADIR=$MYSQL_HOME/data
  #   export MYSQL_UNIX_PORT=$MYSQL_HOME/mysql.sock
  #   MYSQL_PID_FILE=$MYSQL_HOME/mysql.pid
  #   alias mysql='mysql -u root'
  #
  #   if [ ! -d "$MYSQL_HOME" ]; then
  #     # Make sure to use normal authentication method otherwise we can only
  #     # connect with unix account. But users do not actually exists in nix.
  #     mysql_install_db --auth-root-authentication-method=normal \
  #       --datadir=$MYSQL_DATADIR --basedir=$MYSQL_BASEDIR \
  #       --pid-file=$MYSQL_PID_FILE
  #   fi
  #
  #   # Starts the daemon
  #   mysqld --datadir=$MYSQL_DATADIR --pid-file=$MYSQL_PID_FILE \
  #     --socket=$MYSQL_UNIX_PORT 2> $MYSQL_HOME/mysql.log &
  #   MYSQL_PID=$!
  #
  #   finish()
  #   {
  #     mysqladmin -u root --socket=$MYSQL_UNIX_PORT shutdown
  #     kill $MYSQL_PID
  #     wait $MYSQL_PID
  #   }
  #   trap finish EXIT
  # '';
}
