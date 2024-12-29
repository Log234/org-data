let
  pkgs = import <nixpkgs> {};
  sklearn = pkgs.python3Packages.buildPythonPackage rec {
      pname = "evaluate";
      version = "0.4.3";
      src = pkgs.fetchPypi {
        inherit pname version;
        sha256 = "3a5700cf83aabee9549264e1e5666f116367c61dbd4d38352015e859a5e2098d";
      };
    };
in
pkgs.mkShell {
  packages = [
    (pkgs.python312.withPackages (python-pkgs: with python-pkgs; [
      jupyter
      pandas
      evaluate
      datasets
      wandb
      scikit-learn
      transformers
      torch
      accelerate
    ]))
  ];
}
