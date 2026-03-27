import { network } from "hardhat";

async function main() {
  const { ethers } = await network.connect("sepolia");

  const [deployer] = await ethers.getSigners();

  console.log("Deploying contract with account:", deployer.address);

  const token = await ethers.deployContract("CatCoin");
  await token.waitForDeployment();

  const tokenAddress = await token.getAddress();
  console.log("CatCoin deployed to:", tokenAddress);

  const balance = await token.balanceOf(deployer.address);
  console.log("Deployer balance:", ethers.formatUnits(balance, 18));
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});