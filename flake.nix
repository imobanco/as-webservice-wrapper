{
  description = "Flake do as-webservice-wrapper";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let

        pkgsAllowUnfree = import nixpkgs {
          system = "x86_64-linux";
          config = { allowUnfree = true; };
        };

        config = {
          projectDir = ./.;
        };

      in
      {

        poetryEnv = import ./mkPoetryEnv.nix.nix {
          pkgs = nixpkgs.legacyPackages.${system};
        };

        env = pkgsAllowUnfree.poetry2nix.mkPoetryEnv config;

        devShell = pkgsAllowUnfree.mkShell {
          buildInputs = with pkgsAllowUnfree; [
            #(pkgsAllowUnfree.poetry2nix.mkPoetryEnv config)
            gnumake
            poetry
            python3
          ];

          shellHook = ''
            # TODO: documentar esse comportamento,
            # devo abrir issue no github do nixpkgs
            export TMPDIR=/tmp

            echo "Entering the nix devShell"
          '';
        };
      });
}
