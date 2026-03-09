{ pkgs, ... }:

{
  env.GREET = "devenv";

  packages = [
    pkgs.git
    pkgs.uv
  ];

  # enable .env for API keys
  #dotenv.enable = true;

  languages = {
    python = {
      enable = true;
      version = "3.13";
      venv.enable = true;

      venv.requirements = ''
        coverage
        python-dotenv
      '';

      uv = {
        enable = true;
        sync.enable = true; # handles pyproject.toml install
      };

      libraries = [
        pkgs.python313Packages.python-dotenv
      ];
    };
  };

  enterShell = ''
    echo "Boot.dev SSG project devenv"
  '';
}
